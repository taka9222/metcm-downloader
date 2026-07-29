from nicegui import ui
import asyncio

from services.fnl_fetcher import get_latest_fnl


async def dialog_latest_weather():

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


def _dialog_result(result):

    if result is None:
        ui.notify('気象データの取得に失敗しました', color='negative')
        return

    with ui.dialog() as dialog, ui.card().classes('w-96'):
        ui.label('最新の気象データ').classes('text-h6')
        ui.separator()
        ui.label(result["filename"]).classes('text-bold')
        ui.label(result["time"].strftime('%Y年 %m月 %d日 %H00 UTC'))
        ui.space()
        with ui.row().classes('justify-end'):
            ui.button('過去データを検索', on_click=lambda: search_history(dialog))
            ui.button('日付を指定', on_click=lambda: search_by_date(dialog))
            ui.button('ダウンロード開始', on_click=lambda: start_download(result, dialog)).props('color=primary')
            ui.button('キャンセル', on_click=dialog.close)

    dialog.open()