from nicegui import ui
from datetime import datetime, timezone
import asyncio
import traceback

from services.fnl_fetcher import get_latest_fnl
from services.fnl_downloader import start_download, search_by_date


def hours_ago(t: datetime) -> float:
    """UTC datetime t が現在から何時間前かを返す。"""
    return (datetime.now(timezone.utc) - t).total_seconds() / 3600


async def dialog_latest_weather_old(lat: float, lon: float):
    loading = ui.dialog().props(
        'transition-show="fade" '
        'transition-hide="fade"'
    )

    with loading:
        with ui.card().classes('loading-card'):
            with ui.column().classes('items-center w-full'):
                ui.spinner(size='42px', color='primary')
                ui.label('最新データを検索しています').classes('loading-message')

    loading.open()
    await asyncio.sleep(0)
    try:
        result = await asyncio.to_thread(
            get_latest_fnl
        )
    except Exception as e:
        ui.notify(f'検索エラー: {e}', color='negative')
        result = None
    finally:
        loading.close()

    _dialog_result(result)


async def dialog_latest_weather(lat: float, lon: float):
    with ui.dialog() as loading_dialog:
        with ui.card().classes('weather-dialog'):
            ui.label('LATEST DATA').classes('dialog-eyebrow')
            ui.label('最新データを取得中').classes('dialog-title')
            ui.separator().classes('dialog-separator')
            ui.spinner('dots').classes('text-primary')

    loading_dialog.open()
    await asyncio.sleep(0)

    try:
        result = await asyncio.to_thread(get_latest_fnl)

    except Exception as e:
        loading_dialog.close()
        ui.notify(
            f'気象データの取得に失敗しました: {e}',
            color='negative',
        )
        traceback.print_exc()
        return

    loading_dialog.close()

    if result is None:
        ui.notify('最新のFNLデータが見つかりません', color='negative')
        return

    _dialog_result(result, lat, lon)


def _dialog_result(result, lat, lon):
    if result is None:
        ui.notify('気象データの取得に失敗しました', color='negative')
        return

    with ui.dialog() as dialog:
        with ui.card().classes('weather-dialog'):

            # Header
            ui.label('WEATHER DATA').classes('dialog-eyebrow')
            ui.label('最新の気象データ').classes('dialog-title')
            ui.separator().classes('dialog-separator')

            # Data
            timestamp = result["time"].strftime('%Y年 %m月 %d日 %H00 UTC')
            elapsed = round(hours_ago(result["time"]))

            with ui.column().classes('dialog-info'):
                ui.label('LATEST OBSERVATION').classes('dialog-section-label')
                ui.label(timestamp).classes('dialog-time')
                ui.label(f'{elapsed} 時間前のデータ').classes('dialog-age')

                with ui.row().classes('dialog-file-row'):
                    ui.icon('description').classes('dialog-file-icon')
                    ui.label(result["filename"]).classes('dialog-filename')

            ui.space()

            # Actions
            with ui.row().classes('dialog-actions'):

                ui.button('ダウンロード開始', on_click=lambda: start_download(result, dialog, lat, lon)).props('unelevated').classes('dialog-primary-button')
                ui.button('日付を指定', on_click=lambda: search_by_date(dialog, lat, lon)).props('flat').classes('dialog-button')
                ui.button('キャンセル', on_click=dialog.close).props('flat').classes('dialog-cancel-button')

    dialog.open()