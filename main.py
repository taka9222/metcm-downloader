from nicegui import app, ui
from functools import wraps
import os

from static.head import add_head
from pages.home import home_page
from pages.locations import locations_page
from pages.locations_map import map_page
from pages.result import result_page
from pages.settings import settings_page
from pages.help import help_page
from components.appearance import apply_appearance


# _original_run_javascript = ui.run_javascript


# def debug_run_javascript(*args, **kwargs):
#     print("=== ui.run_javascript called ===")
#     print(args)
#     print(kwargs)
#     import traceback
#     traceback.print_stack()
#     return _original_run_javascript(*args, **kwargs)


# ui.run_javascript = debug_run_javascript


def themed_page(page):
    @wraps(page)
    def wrapper(*args, **kwargs):
        theme = app.storage.user.get("appearance", "system")
        apply_appearance(theme)
        return page(*args, **kwargs)

    return wrapper


# PWA化
app.add_static_files("/static", "static")

add_head()

ui.sub_pages({
    "/": themed_page(home_page),
    "/locations": themed_page(locations_page),
    "/map/{lat}/{lon}": themed_page(map_page),
    "/result": themed_page(result_page),
    "/settings": themed_page(settings_page),
    "/help": themed_page(help_page),
}).classes("w-full")

port = int(os.environ.get("PORT", 8080))

ui.run(
    title="METCM Downloader",
    favicon="static/icon-512.png",  # とりあえずPWAアイコン
    host="0.0.0.0",
    port=port,
    storage_secret="6d2740f2fcfc818d68a39f9d6654db89718db917f1b872e4545cf7c9b91f72e3",
)
