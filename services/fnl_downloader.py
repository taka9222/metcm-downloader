import os
import asyncio
from nicegui import ui
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, build_opener, urlopen

from .atmosphere import get_atmospheric_layers
from components.result import _show_atmospheric_layers

FNL_BASE_URL = ("https://osdf-director.osg-htc.org/ncar/gdex/d083002/grib2")
FNL_HOURS = (0, 6, 12, 18)
DOWNLOAD_DIR = Path("/tmp/fnl")


def make_fnl_url(dt: datetime) -> str:
    """UTC日時からFNL GRIB2のURLを生成する."""
    dt = dt.astimezone(timezone.utc)
    return f"{FNL_BASE_URL}/{dt:%Y}/{dt:%Y.%m}/fnl_{dt:%Y%m%d_%H}_00.grib2"


def check_exists(url: str) -> bool:
    """URLのファイルが存在するかHEADで確認する."""
    try:
        req = Request(url, method="HEAD")
        with urlopen(req, timeout=10) as response:
            return response.status == 200
    except (HTTPError, URLError, TimeoutError):
        return False


def download_fnl(url: str) -> Path:
    """FNL GRIB2をダウンロードしてPathを返す."""
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

    output_path = DOWNLOAD_DIR / os.path.basename(url)
    temp_path = output_path.with_suffix(".grib2.part")

    if output_path.exists() and output_path.stat().st_size > 0:
        print(f"Using cached file: {output_path}")
        return output_path

    temp_path.unlink(missing_ok=True)

    print(f"Downloading: {url}")
    print(f"Output: {output_path}")

    opener = build_opener()

    try:
        with opener.open(url, timeout=60) as infile:
            with temp_path.open("wb") as outfile:
                while chunk := infile.read(1024 * 1024):
                    outfile.write(chunk)

        temp_path.replace(output_path)

    except Exception:
        temp_path.unlink(missing_ok=True)
        raise

    print(f"Download complete: {output_path}")
    print(f"File size: {output_path.stat().st_size:,} bytes")

    return output_path


def search_by_date(parent_dialog, lat: float, lon: float):
    parent_dialog.close()

    with ui.dialog() as dialog:
        with ui.card().classes('weather-dialog'):

            ui.label('DATA SEARCH').classes('dialog-eyebrow')
            ui.label('日付を指定').classes('dialog-title')
            ui.separator().classes('dialog-separator')

            ui.label('SELECT DATE').classes('dialog-section-label')

            date_input = ui.date().props(
                'mask=YYYY-MM-DD'
            ).classes('w-full')

            ui.space()

            with ui.row().classes('dialog-actions'):
                ui.button(
                    'キャンセル',
                    on_click=dialog.close,
                ).props('flat').classes('dialog-cancel-button')

                ui.button(
                    '検索',
                    on_click=lambda: _search_fnl_date(
                        date_input.value,
                        dialog,
                        lat,
                        lon,
                    ),
                ).props('unelevated').classes('dialog-primary-button')

    dialog.open()


async def _search_fnl_date(
    date_value,
    dialog,
    lat: float,
    lon: float,
):
    if not date_value:
        ui.notify('日付を選択してください', color='warning')
        return

    try:
        selected_date = date.fromisoformat(date_value)
    except ValueError:
        ui.notify('日付の形式が正しくありません', color='negative')
        return

    dialog.close()

    with ui.dialog() as loading_dialog:
        with ui.card().classes('weather-dialog'):
            ui.label('SEARCHING').classes('dialog-eyebrow')
            ui.label('データを検索中').classes('dialog-title')
            ui.separator().classes('dialog-separator')

            ui.spinner('dots').classes('text-primary')

            ui.label(
                f'{selected_date:%Y年 %m月 %d日} のFNLデータを確認しています'
            ).classes('dialog-age')

    loading_dialog.open()
    await asyncio.sleep(0)

    try:
        results = await asyncio.to_thread(
            _find_fnl_files,
            selected_date,
        )
    finally:
        loading_dialog.close()

    _show_fnl_search_results(
        results,
        selected_date,
        lat,
        lon,
    )


def _find_fnl_files(selected_date: date) -> list[dict]:
    """指定日の00/06/12/18 UTCのFNLファイルを検索する."""
    results = []

    for hour in FNL_HOURS:
        dt = datetime(selected_date.year, selected_date.month, selected_date.day, hour, tzinfo=timezone.utc)
        url = make_fnl_url(dt)

        results.append({
            'time': dt, 'url': url, 'filename': os.path.basename(url), 'exists': check_exists(url),
        })

    return results


def _show_fnl_search_results(
    results: list[dict],
    selected_date: date,
    lat: float,
    lon: float,
):
    with ui.dialog() as dialog:
        with ui.card().classes('weather-dialog'):

            ui.label('AVAILABLE DATA').classes('dialog-eyebrow')
            ui.label('取得可能なデータ').classes('dialog-title')
            ui.separator().classes('dialog-separator')

            ui.label(
                selected_date.strftime('%Y年 %m月 %d日')
            ).classes('dialog-time')

            ui.label('UTC').classes('dialog-age')

            with ui.column().classes('fnl-results'):
                for result in results:
                    _add_fnl_result_row(
                        result,
                        dialog,
                        lat,
                        lon,
                    )

            ui.space()

            with ui.row().classes('dialog-actions'):
                ui.button(
                    '閉じる',
                    on_click=dialog.close,
                ).props('flat').classes('dialog-cancel-button')

    dialog.open()


def _add_fnl_result_row(
    result: dict,
    dialog,
    lat: float,
    lon: float,
):
    available = result['exists']
    dt = result['time']

    with ui.row().classes('fnl-result-row'):
        with ui.column().classes('fnl-result-info'):
            ui.label(
                dt.strftime('%H00 UTC')
            ).classes('fnl-result-time')

            ui.label(
                result['filename']
            ).classes('fnl-result-filename')

        if available:
            ui.label('AVAILABLE').classes('fnl-available')

            ui.button(
                'ダウンロード',
                on_click=lambda r=result: start_download(
                    r,
                    dialog,
                    lat,
                    lon,
                ),
            ).props('unelevated').classes('dialog-primary-button')
        else:
            ui.label('NOT AVAILABLE').classes('fnl-unavailable')


async def start_download(result: dict, dialog, lat: float, lon: float):
    dialog.close()

    with ui.dialog() as loading_dialog:
        with ui.card().classes('weather-dialog'):
            ui.label('DOWNLOAD').classes('dialog-eyebrow')
            ui.label('データを取得中').classes('dialog-title')
            ui.separator().classes('dialog-separator')

            ui.spinner('dots').classes('text-primary')

            ui.label(result['filename']).classes('dialog-filename')
            ui.label(
                'FNL GRIB2データをダウンロードしています'
            ).classes('dialog-age')

    loading_dialog.open()
    await asyncio.sleep(0)

    try:
        file = await asyncio.to_thread(
            download_fnl,
            result['url'],
        )

    except Exception as e:
        loading_dialog.close()
        ui.notify(
            f'ダウンロードに失敗しました: {e}',
            color='negative',
        )
        return

    # ---------------------------------------------------------
    # ダウンロード完了 → 気象データ解析
    # ---------------------------------------------------------

    loading_dialog.clear()

    with loading_dialog:
        with ui.card().classes('weather-dialog'):
            ui.label('ANALYSIS').classes('dialog-eyebrow')
            ui.label('気象データを解析中').classes('dialog-title')
            ui.separator().classes('dialog-separator')

            ui.spinner('dots').classes('text-primary')

            ui.label(
                f'緯度 {lat:.4f} / 経度 {lon:.4f}'
            ).classes('dialog-time')

            ui.label(
                '大気層データを計算しています'
            ).classes('dialog-age')

    await asyncio.sleep(0)

    try:
        layers = await asyncio.to_thread(
            get_atmospheric_layers,
            file,
            lat,
            lon,
            maximum_zone=16,
        )

    except Exception as e:
        loading_dialog.close()
        ui.notify(f'気象データの解析に失敗しました: {e}', color='negative', position="top")
        return

    loading_dialog.close()

    _show_atmospheric_layers(
        layers,
        result,
        lat,
        lon,
    )