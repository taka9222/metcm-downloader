from datetime import datetime, timedelta, timezone
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import time


BASE_URL = (
    "https://osdf-director.osg-htc.org/ncar/gdex/d083002/grib2/"
)


def check_exists(url: str, timeout: float = 1.0, retries: int = 3) -> bool:
    """ファイルの存在確認（本体は取得しない）"""
    for attempt in range(retries + 1):
        try:
            req = Request(url, method="HEAD")
            with urlopen(req, timeout=timeout) as response:
                return response.status == 200

        except HTTPError as e:
            print(e.code, url)
            # 404などはリトライせず「存在しない」と判定
            if e.code == 404:
                return False

        except (URLError, TimeoutError):
            pass

        if attempt < retries:
            time.sleep(0.2)

    return False


def generate_fnl_url(dt):
    filename = dt.strftime("fnl_%Y%m%d_%H_00.grib2")
    return f"{BASE_URL}{dt.strftime('%Y')}/{dt.strftime('%Y.%m')}/{filename}"


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
        url = generate_fnl_url(t)
        if check_exists(url):
            print(url)
            return {"time": t, "url": url, "filename": url.split("/")[-1]}
        t -= timedelta(hours=6)
    return None


def main():
    latest = get_latest_fnl()
    if latest:
        print(latest["filename"])
        print(latest["url"])
    else:
        print("FNL not found")


if __name__ == "__main__":
    main()