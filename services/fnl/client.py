from __future__ import annotations

from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import time


FNL_BASE_URL = (
    "https://osdf-director.osg-htc.org/ncar/gdex/d083002/grib2"
)

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