import asyncio
from nicegui import ui
from datetime import date

from services.atmosphere import get_atmospheric_layers
from services.fnl.downloader import download_fnl
from services.fnl.search import find_fnl_files
from components.result import _show_atmospheric_layers

FNL_HOURS = (0, 6, 12, 18)


def search_by_date(parent_dialog, lat: float, lon: float):
    parent_dialog.close()

    with ui.dialog() as dialog:
        with ui.card().classes('weather-dialog'):

            ui.label('DATA SEARCH').classes('dialog-eyebrow')
            ui.label('日付を指定').classes('dialog-title')
            ui.separator().classes('dialog-separator')

            ui.label('SELECT DATE').classes('dialog-section-label')

            date_input = ui.date().props('mask=YYYY-MM-DD').classes('w-full')

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
        results = await asyncio.to_thread( find_fnl_files, selected_date)
    finally:
        loading_dialog.close()

    _show_fnl_search_results(results, selected_date, lat, lon)


def _show_fnl_search_results(
    results: list[dict],  # list[dataClass]
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
    result: dict,  # dataClass
    dialog, lat: float, lon: float,
):
    available = result.exists
    dt = result.time

    with ui.row().classes('fnl-result-row'):

        with ui.column().classes('fnl-result-info'):

            ui.label(dt.strftime('%H00 UTC')).classes('fnl-result-time')
            ui.label(result.filename).classes('fnl-result-filename')

        if available:

            ui.label('AVAILABLE').classes('fnl-available')
            ui.button(
                'ダウンロード', on_click=lambda r=result: start_download(r, dialog, lat, lon)
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

            ui.label(result.filename).classes('dialog-filename')
            ui.label(
                'FNL GRIB2データをダウンロードしています'
            ).classes('dialog-age')

    loading_dialog.open()
    await asyncio.sleep(0)

    try:
        file = await asyncio.to_thread(
            download_fnl,
            result.url,
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
        # layers = get_atmospheric_layers(file, lat, lon, maximum_zone=16)
        layers = await asyncio.to_thread(get_atmospheric_layers, file, lat, lon, maximum_zone=16)

    except Exception as e:
        loading_dialog.close()
        ui.notify(f'気象データの解析に失敗しました: {file}, {e}', color='negative', position="top")
        return

    loading_dialog.close()

    _show_atmospheric_layers(layers, result, lat, lon)