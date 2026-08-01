"""
atmospheric_layers.py

FNL GRIB2から指定地点の気象データを取得し、定義された26気層ごとの代表気象値を計算する。

必要:
    pip install numpy scipy eccodes
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from functools import lru_cache
from pathlib import Path

import eccodes
import numpy as np
from scipy.interpolate import RectBivariateSpline


# ============================================================
# 気層定義
# ============================================================

@dataclass(frozen=True)
class AtmosphericZone:
    code: int
    bottom: float
    top: float
    height: float


ATMOSPHERIC_ZONES = [
    AtmosphericZone(1, 0, 200, 100), AtmosphericZone(2, 200, 500, 350),
    AtmosphericZone(3, 500, 1000, 750), AtmosphericZone(4, 1000, 1500, 1250),
    AtmosphericZone(5, 1500, 2000, 1750), AtmosphericZone(6, 2000, 3000, 2500),
    AtmosphericZone(7, 3000, 4000, 3500), AtmosphericZone(8, 4000, 5000, 4500),
    AtmosphericZone(9, 5000, 6000, 5500), AtmosphericZone(10, 6000, 8000, 7000),
    AtmosphericZone(11, 8000, 10000, 9000), AtmosphericZone(12, 10000, 12000, 11000),
    AtmosphericZone(13, 12000, 14000, 13000), AtmosphericZone(14, 14000, 16000, 15000),
    AtmosphericZone(15, 16000, 18000, 17000), AtmosphericZone(16, 18000, 20000, 19000),
    AtmosphericZone(17, 20000, 22000, 21000), AtmosphericZone(18, 22000, 24000, 23000),
    AtmosphericZone(19, 24000, 26000, 25000), AtmosphericZone(20, 26000, 28000, 27000),
    AtmosphericZone(21, 28000, 30000, 29000), AtmosphericZone(22, 30000, 32000, 31000),
    AtmosphericZone(23, 32000, 34000, 33000), AtmosphericZone(24, 34000, 36000, 35000),
    AtmosphericZone(25, 36000, 38000, 37000), AtmosphericZone(26, 38000, 40000, 39000),
]


# ============================================================
# データ構造
# ============================================================

@dataclass
class PressureLevelData:
    """1つの気圧面についてのデータ."""

    level: float
    height: float | None = None
    density: float | None = None
    temperature: float | None = None
    virtual_temperature: float | None = None
    relative_humidity: float | None = None
    specific_humidity: float | None = None
    u_wind: float | None = None
    v_wind: float | None = None


@dataclass
class AtmosphericLayer:
    """1気層の代表値."""

    zone: int
    bottom: float
    top: float
    height: float
    density: float | None = None
    temperature: float | None = None
    virtual_temperature: float | None = None
    pressure: float | None = None
    wind_speed: float | None = None
    wind_direction: float | None = None
    relative_humidity: float | None = None
    specific_humidity: float | None = None


# ============================================================
# GRIB読み込み
# ============================================================

REQUIRED_VARIABLES = {"gh", "t", "r", "q", "u", "v"}


def print_tree(d, level=0):
    for key, value in d.items():
        print("  " * level + f"- {key}")
        if isinstance(value, dict):
            print_tree(value, level + 1)
        elif value.any():
            print("  " * (level + 1) + f"= {value}")


def _make_local_grid(latitudes: np.ndarray, longitudes: np.ndarray, latitude: float, longitude: float, neighbor_radius: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """指定地点の近傍だけを切り出すための格子情報を作る."""

    if neighbor_radius < 2:
        raise ValueError("neighbor_radius must be at least 2 for cubic spline.")

    grid_lat = np.asarray(latitudes)
    grid_lon = np.asarray(longitudes) % 360
    lat_values = np.unique(grid_lat)
    lon_values = np.unique(grid_lon)

    if lat_values.size * lon_values.size != grid_lat.size:
        raise ValueError("GRIB grid is not a regular latitude/longitude grid.")

    lat_values = np.sort(lat_values)
    lon_values = np.sort(lon_values)

    # GRIB内部の格子順に依存せず、
    # 「緯度×経度」の位置から元の1次元配列インデックスを作る。
    order = np.lexsort((grid_lon, grid_lat))
    sorted_lat = grid_lat[order].reshape(lat_values.size, lon_values.size)
    sorted_lon = grid_lon[order].reshape(lat_values.size, lon_values.size)

    if not np.all(sorted_lat == lat_values[:, None]):
        raise ValueError("Unexpected latitude ordering in GRIB grid.")
    if not np.all(sorted_lon == lon_values[None, :]):
        raise ValueError("Unexpected longitude ordering in GRIB grid.")

    target_lon = longitude % 360
    lat_center = int(np.argmin(np.abs(lat_values - latitude)))
    lon_center = int(np.argmin(np.abs(lon_values - target_lon)))

    lat_start = max(0, lat_center - neighbor_radius)
    lat_end = min(lat_values.size, lat_center + neighbor_radius + 1)
    lat_indices = np.arange(lat_start, lat_end)

    # 経度は周期境界なので、0/360度を跨いでも連続した近傍を取得する。
    lon_indices = (np.arange(lon_center - neighbor_radius, lon_center + neighbor_radius + 1) % lon_values.size)

    # sorted_lat/sorted_lon上の位置から、元のGRIB valuesのindexへ戻す。
    sorted_indices = order.reshape(lat_values.size, lon_values.size)
    indices = sorted_indices[lat_indices[:, None], lon_indices[None, :]].ravel()

    return (lat_values[lat_indices], lon_values[lon_indices], indices)


def _build_spline(values: np.ndarray, latitudes: np.ndarray, longitudes: np.ndarray) -> RectBivariateSpline:
    """局所的な規則格子から3次スプラインを構築する."""

    if not np.all(np.isfinite(values)):
        raise ValueError("Spline interpolation requires finite grid values.")

    lat = np.asarray(latitudes)
    lon = np.asarray(longitudes)

    # 経度の周期境界を跨ぐ場合、値の順序を0～360度の連続した順序に戻す。
    lon_order = np.argsort(lon)
    lon = lon[lon_order]

    nlat = lat.size
    nlon = lon.size
    grid = values.reshape(nlat, nlon)[:, lon_order]

    # 緯度はRectBivariateSplineが要求する昇順に統一。
    lat_order = np.argsort(lat)
    lat = lat[lat_order]
    grid = grid[lat_order]

    return RectBivariateSpline(lat, lon, grid, kx=min(3, nlat - 1), ky=min(3, nlon - 1), s=0)


def _read_grib(path: str, lat: float, lon: float, neighbor_radius: int) -> dict:
    """GRIB2を読み込み、指定地点近傍の格子だけを保持する."""

    path_obj = Path(path)
    if not path_obj.exists():
        raise FileNotFoundError(path_obj)

    data = {variable: {} for variable in REQUIRED_VARIABLES}
    local_grid = None

    with path_obj.open("rb") as f:
        while True:
            gid = eccodes.codes_grib_new_from_file(f)
            if gid is None:
                break

            try:
                short_name = eccodes.codes_get(gid, "shortName")
                if short_name not in REQUIRED_VARIABLES:
                    continue
                if eccodes.codes_get(gid, "typeOfLevel") != "isobaricInhPa":
                    continue

                level = float(eccodes.codes_get(gid, "level"))
                latitudes = np.asarray(eccodes.codes_get_array(gid, "latitudes"), dtype=float)
                longitudes = np.asarray(eccodes.codes_get_array(gid, "longitudes"), dtype=float)
                values = np.asarray(eccodes.codes_get_array(gid, "values"), dtype=float)

                if local_grid is None:
                    local_lat, local_lon, indices = _make_local_grid(
                        latitudes, longitudes, lat, lon, neighbor_radius,
                    )
                    local_grid = {"lat": local_lat, "lon": local_lon, "indices": indices}

                local_values = values[local_grid["indices"]]

                data[short_name][level] = {
                    "values": local_values,
                    "spline": None,
                    "wrapped_spline": None,
                }
            finally:
                eccodes.codes_release(gid)

    if local_grid is None:
        raise ValueError("No required isobaric data found in GRIB2.")

    data["_grid"] = local_grid
    return data


@lru_cache(maxsize=2)
def _read_grib_cached(path: str, mtime_ns: int, lat: float, lon: float, neighbor_radius: int) -> dict:
    """同じGRIB・地点・近傍サイズなら読み込み結果を再利用する."""
    return _read_grib(path, lat, lon, neighbor_radius)


def read_grib(path: str | Path, lat: float, lon: float, neighbor_radius: int = 2) -> dict:
    """GRIB2から指定地点近傍の格子だけを読み込む."""
    path_obj = Path(path).resolve()
    if not path_obj.exists():
        raise FileNotFoundError(path_obj)

    return _read_grib_cached(
        str(path_obj), path_obj.stat().st_mtime_ns, float(lat), float(lon), int(neighbor_radius),
    )


def interpolate_at_point(
    message: dict, grid: dict, latitude: float, longitude: float,
) -> float | None:
    """指定地点近傍の格子だけを使って3次スプライン補間する."""
    values = message["values"]
    if not np.any(np.isfinite(values)):
        return None

    lat = grid["lat"]
    lon = grid["lon"]
    target_lon = longitude % 360

    if not lat[0] <= latitude <= lat[-1]:
        return None

    # 0/360度境界を跨ぐ局所格子は、経度を連続化してからSplineを構築する。
    if np.ptp(lon) > 180:
        wrapped_lon = np.where(lon < 180, lon + 360, lon)
        target_lon = target_lon + 360 if target_lon < 180 else target_lon

        spline = message["wrapped_spline"]
        if spline is None:
            order = np.argsort(wrapped_lon)
            spline = RectBivariateSpline(
                lat, wrapped_lon[order], values.reshape(lat.size, lon.size)[:, order],
                kx=min(3, lat.size - 1), ky=min(3, lon.size - 1), s=0,
            )
            message["wrapped_spline"] = spline
    else:
        spline = message["spline"]
        if spline is None:
            spline = _build_spline(values, lat, lon)
            message["spline"] = spline

    if target_lon < spline.get_knots()[1][0] or target_lon > spline.get_knots()[1][-1]:
        return None

    return float(spline.ev(latitude, target_lon))


# ============================================================
# 指定地点の気圧面データ取得
# ============================================================

def extract_pressure_levels(
    grib_data: dict, latitude: float, longitude: float,
) -> list[PressureLevelData]:
    """
    指定地点について各気圧面のデータを取得する。

    入力:
        grib_data
          │
          ├─ gh ─→ 1000hPa ─→ 格子データ
          │       925hPa ─→ 格子データ
          │       850hPa ─→ 格子データ
          │       ...
          ├─ t  ─→ 同上
          ├─ r  ─→ 同上
          ├─ u  ─→ 同上
          └─ v  ─→ 同上

        指定地点:
            latitude  = 35.0
            longitude = 136.0

                 GRIB格子
                    │
                    ├─ gh ─→ 補間 ─→ 高度
                    ├─ t  ─→ 補間 ─→ 気温
                    ├─ r  ─→ 補間 ─→ 湿度
                    ├─ u  ─→ 補間 ─→ U風
                    └─ v  ─→ 補間 ─→ V風

    出力:
        list[PressureLevelData]

        [
            PressureLevelData(
                level=1000,
                height=...
                temperature=...
                relative_humidity=...
                u_wind=...
                v_wind=...
            ),
            PressureLevelData(
                level=925,
                ...
            ),
            ...
        ]

        つまり、

        気圧面ごとのGRIB格子
                 ↓
             指定地点へ補間
                 ↓
        [気圧面 × 気象要素]
                 ↓
        高度順の1次元データ
    """

    # すべての変数に共通するlevelだけを抽出
    levels = sorted(set.intersection(*(set(grib_data[v]) for v in REQUIRED_VARIABLES)), reverse=True)
    grid = grib_data["_grid"]
    result = []

    for level in levels:
        values = {
            variable: interpolate_at_point(grib_data[variable][level], grid, latitude, longitude)
            for variable in REQUIRED_VARIABLES
        }

        if values["gh"] is None:
            continue

        virtual_temperature = None
        if values["t"] is not None and values["q"] is not None:
            virtual_temperature = float(
                comp_virtual_temperature(
                    np.array([values["t"]]), np.array([values["q"]]),
                )[0]
            )

        density = None
        if virtual_temperature is not None:
            density = float(
                comp_air_den(
                    np.array([virtual_temperature]), np.array([level]),
                )[0]
            )

        result.append(PressureLevelData(
            level=level, height=values["gh"], density=density,
            temperature=values["t"], virtual_temperature=virtual_temperature,
            relative_humidity=values["r"], specific_humidity=values["q"],
            u_wind=values["u"], v_wind=values["v"],
        ))

    result.sort(key=lambda x: x.height)
    return result



# ============================================================
# 高度方向補間
# ============================================================

def interpolate_vertical(
    heights: np.ndarray, values: np.ndarray, target_heights: np.ndarray,
) -> np.ndarray:
    """
    気圧面データを高度方向に線形補間する。
    範囲外はNaN。

    入力:
        気圧面から得られた高度方向のデータ

    処理:
        heights + values
                │
                ▼
        高度方向に線形補間
                │
                ▼
        target_heights上の値

    出力:
        target_heightsと同じshapeのndarray

        heights        values
        [1000, 2000, 3500, 5000]
              ↓ 補間
        target_heights
        [1500, 2500, 3000, 4000]
              ↓
        result
        [  ...,  ...,  ...,  ...]
    """

    valid = np.isfinite(heights) & np.isfinite(values)
    if np.count_nonzero(valid) < 2:
        return np.full(target_heights.shape, np.nan)

    heights, values = heights[valid], values[valid]
    order = np.argsort(heights)
    heights, values = heights[order], values[order]
    heights, unique_indices = np.unique(heights, return_index=True)
    values = values[unique_indices]

    result = np.full(target_heights.shape, np.nan)
    inside = (target_heights >= heights[0]) & (target_heights <= heights[-1])
    result[inside] = np.interp(target_heights[inside], heights, values)
    return result


# ============================================================
# 気層内平均
# ============================================================

def layer_mean(
    heights: np.ndarray, values: np.ndarray, bottom: float, top: float, sample_interval: float = 50.0,
) -> float | None:
    """
    指定高度範囲内を一定間隔でサンプリングし、
    高度方向に線形補間した値の平均を返す。

    入力:
        高度方向データ
            heights ──→ [1000, 2000, 3500, 5000, ...]
            values  ──→ [  10,   12,   15,   18, ...]

        気層:
            bottom = 2000 m
            top    = 3000 m

        sample_interval = 50 m

    処理:

        2000m ──●
                │╲
                │ ╲
                │  ╲
        2500m ──●   ← 補間値
                │    ╲
                │     ╲
        3000m ──●──────●
             ↑  ↑  ↑  ↑
            50m間隔でサンプリング

        [2000, 2050, 2100, ..., 2950, 3000]
                          │
                          ▼
                     線形補間
                          │
                          ▼
                    各高度の値
                          │
                          ▼
                        mean

    出力:
        1つの代表値
            float | None
    """

    if top <= bottom:
        raise ValueError("top must be greater than bottom")

    sample_heights = np.append(np.arange(bottom, top, sample_interval), top)
    sampled_values = interpolate_vertical(heights, values, sample_heights)
    valid = np.isfinite(sampled_values)

    return float(np.mean(sampled_values[valid])) if np.any(valid) else None


# 弾道気温
def comp_virtual_temperature(temperature: np.ndarray, specific_humidity: np.ndarray) -> np.ndarray:
    """気温[K]、湿比から仮温度[K]を求める。"""
    mixing_ratio = specific_humidity / (1.0 - specific_humidity)
    return temperature * (1.0 + 0.6078 * mixing_ratio)

# 空気密度
def comp_air_den(virtual_temperature: np.ndarray, pressure: np.ndarray) -> np.ndarray:
    """弾道気温[K], 気圧[hPa]から空気密度[g/m^3]を求める"""
    return 348.367876 * pressure / virtual_temperature  # 乾燥空気の比気体定数 の逆数


# ============================================================
# 風向・風速
# ============================================================

def uv_to_wind(u: float | None, v: float | None) -> tuple[float | None, float | None]:
    """
    U/V成分から風速・風向を計算する。
    UV成分は「風の流れ」を表すのに対し、風向は「風が吹いてくる方向」となるため符号を反転して変換.
    """

    if u is None or v is None or not np.isfinite(u) or not np.isfinite(v):
        return None, None

    speed = np.hypot(u, v)
    direction = (np.degrees(np.arctan2(-u, -v)) + 360) % 360 
    direction = direction * 3200 / 180
    return float(speed), float(direction)


# ============================================================
# 気層計算
# ============================================================

def calculate_layers(
    pressure_levels: list[PressureLevelData], sample_interval: float = 50.0, maximum_zone: int | None = None,
) -> list[AtmosphericLayer]:
    """各気圧面のデータから気層の代表値を計算する."""

    if not pressure_levels:
        raise ValueError("No pressure-level data available.")

    heights = np.array([x.height for x in pressure_levels], dtype=float)
    order = np.argsort(heights)
    heights = heights[order]

    arrays = {
        name: np.array([
            np.nan if (value := getattr(x, name)) is None else value
            for x in pressure_levels
        ], dtype=float)[order]
        for name in (
            "density", "temperature", "virtual_temperature", "level",
            "relative_humidity", "specific_humidity", "u_wind", "v_wind",
        )
    }
    # arrays = {
    #     "temperature": 1013hPaから気圧ごとにその地点での温度を並べたnp.1darray,
    #     " relative_humidity": 気圧ごと湿度のnp.1darray,
    #     ...
    # }

    def mean(values: np.ndarray, zone: AtmosphericZone) -> float | None:
        return layer_mean(
            heights, values, zone.bottom, zone.top, sample_interval,
        )

    layers = []
    for zone in ATMOSPHERIC_ZONES[:maximum_zone]:
        density = mean(arrays["density"], zone)
        temperature = mean(arrays["temperature"], zone)
        virtual_temperature = mean(arrays["virtual_temperature"], zone)
        pressure = mean(arrays["level"], zone)
        relative_humidity = mean(arrays["relative_humidity"], zone)
        specific_humidity = mean(arrays["specific_humidity"], zone)
        u_mean = mean(arrays["u_wind"], zone)
        v_mean = mean(arrays["v_wind"], zone)
        wind_speed, wind_direction = uv_to_wind(u_mean, v_mean)

        layers.append(AtmosphericLayer(
            zone=zone.code, bottom=zone.bottom, top=zone.top, height=zone.height,
            density=density, temperature=temperature, virtual_temperature=virtual_temperature,
            pressure=pressure, wind_speed=wind_speed, wind_direction=wind_direction,
            relative_humidity=relative_humidity, specific_humidity=specific_humidity,
        ))

    return layers



# ============================================================
# メインAPI
# ============================================================

def get_atmospheric_layers(
    grib_path: str | Path, latitude: float, longitude: float, 
    sample_interval: float = 50.0, maximum_zone: int | None = None, neighbor_radius: int = 2,
) -> list[dict]:
    """GRIB2から指定地点の26気層の気象データを取得する."""

    if maximum_zone is not None and not 1 <= maximum_zone <= len(ATMOSPHERIC_ZONES):
        raise ValueError(f"maximum_zone must be between 1 and {len(ATMOSPHERIC_ZONES)}")

    grib_data = read_grib(grib_path, latitude, longitude, neighbor_radius)
    pressure_levels = extract_pressure_levels(grib_data, latitude, longitude)
    return [asdict(layer) for layer in calculate_layers(pressure_levels, sample_interval, maximum_zone)]


# ============================================================
# 動作確認
# ============================================================

if __name__ == "__main__":
    result = get_atmospheric_layers("fnl_20260731_00_00.grib2", 35.0, 136.0, maximum_zone=16)
    for layer in result:
        print(
            f"Zone {layer['zone']:02d} {layer['bottom']:>5.0f}-{layer['height']:>5.0f}-{layer['top']:<5.0f} m | "
            f"rho: {round(layer['density']):04d} | T: {layer['temperature']:5.1f} | Tv: {layer['virtual_temperature']:5.1f} | "
            f"P: {round(layer['pressure']):04d} | WS: {layer['wind_speed']:4.1f} | WD: {round(layer['wind_direction']):04d} | "
            f"RH: {layer['relative_humidity']:6.3f}"
        )
