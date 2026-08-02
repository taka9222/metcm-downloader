from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path

from .client import FNL_HOURS, check_exists, make_fnl_url


@dataclass(frozen=True)
class FNLFile:
    time: datetime
    url: str
    filename: str
    exists: bool


def find_fnl_files(selected_date: date) -> list[FNLFile]:
    """指定日のFNLファイルを検索する."""
    results = []

    for hour in FNL_HOURS:
        dt = datetime(
            selected_date.year,
            selected_date.month,
            selected_date.day,
            hour,
            tzinfo=timezone.utc,
        )

        url = make_fnl_url(dt)

        results.append(
            FNLFile(
                time=dt,
                url=url,
                filename=Path(url).name,
                exists=check_exists(url),
            )
        )

    return results