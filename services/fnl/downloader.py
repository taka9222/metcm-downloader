from __future__ import annotations

import os
from pathlib import Path
from urllib.request import build_opener

from utils.logging import debug_log


DOWNLOAD_DIR = Path("/tmp/fnl")


def download_fnl(url: str) -> Path:
    """FNL GRIB2をダウンロードしてPathを返す."""
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

    output_path = DOWNLOAD_DIR / os.path.basename(url)
    temp_path = output_path.with_suffix(".grib2.part")

    if output_path.exists() and output_path.stat().st_size > 0:
        debug_log(f"Using cached file: {output_path}")
        return output_path

    temp_path.unlink(missing_ok=True)

    debug_log(f"Downloading: {url}")
    debug_log(f"Output: {output_path}")

    opener = build_opener()

    try:
        with opener.open(url, timeout=60) as infile:
            with temp_path.open("wb") as outfile:
                while chunk := infile.read(1024 * 1024):
                    outfile.write(chunk)

        temp_path.replace(output_path)

    except Exception:
        debug_log(f"Download failed: {type(e).__name__}: {e}")
        temp_path.unlink(missing_ok=True)
        raise

    debug_log(f"Download complete: {output_path}") 
    debug_log(f"File size: {output_path.stat().st_size:,} bytes")

    return output_path