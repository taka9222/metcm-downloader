from __future__ import annotations

from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


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


def check_exists(url: str) -> bool:
    """URLのファイルが存在するかHEADで確認する."""
    try:
        request = Request(url, method="HEAD")

        with urlopen(request, timeout=10) as response:
            return response.status == 200

    except (HTTPError, URLError, TimeoutError):
        return False