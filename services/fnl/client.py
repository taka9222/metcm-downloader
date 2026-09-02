from __future__ import annotations

from datetime import datetime, timedelta, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import time

from .data import FNLFile


# FNL_BASE_URL = "https://osdf-director.osg-htc.org/ncar/gdex/d083002/grib2"
FNL_BASE_URL = "https://data.gdex.ucar.edu/d083002/grib2"

FNL_HOURS = (0, 6, 12, 18)


def make_fnl_url(dt: datetime) -> str:
    """UTC日時からFNL GRIB2のURLを生成する."""
    dt = dt.astimezone(timezone.utc)

    return (
        f"{FNL_BASE_URL}/"
        f"{dt:%Y}/{dt:%Y.%m}/"
        f"fnl_{dt:%Y%m%d_%H}_00.grib2"
    )


def check_exists(url: str, timeout: float = 3, retries: int = 2) -> bool:
    """ファイルの存在確認（本体は取得しない）"""
    print(f"Checking existence of {url}...")
    for attempt in range(retries + 1):
        try:
            req = Request(url, method="HEAD")
            with urlopen(req, timeout=timeout) as response:
                return response.status == 200

        except HTTPError as e:
            if e.code == 404:
                return False

        except (URLError, TimeoutError):
            pass

        if attempt < retries:
            time.sleep(0.2)

    return False


def get_latest_fnl():
    """
    利用可能な最新FNLファイルを1つ返す

    Returns
    -------
    dict or None
    """
    now = datetime.now(timezone.utc)
    # 6時間単位に丸める
    hour = (now.hour // 6) * 6
    t = now.replace(hour=hour, minute=0, second=0, microsecond=0)
    t -= timedelta(hours=6)
    # 最大7日探索
    for _ in range(28):
        url = make_fnl_url(t)
        if check_exists(url):
            print(url)
            return FNLFile(
                time=t,
                url=url,
                filename=url.split("/")[-1],
                exists=True,
            )
        t -= timedelta(hours=6)
    return None