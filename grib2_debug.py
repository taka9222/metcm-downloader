import numpy as np
from scipy.interpolate import RectBivariateSpline
import pygrib

def interpolate_grib(grb, lat: float, lon: float) -> dict:
    """GRIB2の2次元格子データから指定緯度経度の値をスプライン補間する。"""

    values = grb.values
    lats, lons = grb.latlons()

    # 1次元の緯度・経度配列を取得
    lat_axis = lats[:, 0]
    lon_axis = lons[0, :]

    # 緯度が南→北になるように並べ替え
    if lat_axis[0] > lat_axis[-1]:
        lat_axis = lat_axis[::-1]
        values = values[::-1, :]

    # 経度が西→東になるように並べ替え
    if lon_axis[0] > lon_axis[-1]:
        lon_axis = lon_axis[::-1]
        values = values[:, ::-1]

    # 2次スプライン補間
    spline = RectBivariateSpline(
        lat_axis,
        lon_axis,
        values,
        kx=3,
        ky=3,
    )

    value = float(spline(lat, lon)[0, 0])

    # np.savetxt("./values.txt", values, fmt="%.3f")
    # np.savetxt("./lats.txt", lats, fmt="%.3f")
    # np.savetxt("./lons.txt", lons, fmt="%.3f")

    return {
        "value": value,
        "typeOfLevel": grb.typeOfLevel,
        "level": grb.level,
        "units": grb.units,
        "name": grb.name,
        "shortName": grb.shortName,

    }

grbs = pygrib.open("./fnl_20260731_00_00.grib2")
for idx, grb in enumerate(grbs):
    print (idx, grb.name, grb.shortName, grb.typeOfLevel, grb.level)
grb = grbs(name="Temperature")[0]

for k in grb.keys():
    try:
        print(k, "\t\t=", grb[k])
    except:
        continue

print("")

for grb in grbs(shortName="v"):
    res = interpolate_grib(grb, 35.0, 136.0)
    print(res)


