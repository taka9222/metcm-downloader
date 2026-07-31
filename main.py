from nicegui import app, ui
import sys
import os
from urllib.request import build_opener
import pygrib

from static.head import add_head
from components.navbar import floating_nav
from components.dialog import dialog_latest_weather
from components.colors import UI_COLORS


def page_header(kicker: str, title: str):
    with ui.column().classes("page-header"):
        ui.label(kicker).classes("page-header-kicker")

        with ui.column().classes("page-header-title-group"):
            ui.label(title).classes("page-header-title")
            ui.element("div").classes("page-header-line")

 
def home_page():
    with ui.column().classes("page-content home-page"):
        page_header("OVERVIEW", "ホーム")
        ui.label("PROTOTYPE UI: overall layout may be altered").classes("home-prototype-note")

        section_header("RECENT LOCATIONS", "直近に使用した演習場")
        location_card(eyebrow="YAUSUBETSU TRAINING AREA", title="矢臼別演習場", region="北海道",
                      coordinate="北緯 43.2997  東経 144.9873", image="/static/images/yausubetsu.jpg", recent=True)
        location_card(eyebrow="HIGASHI FUJI TRAINING AREA", title="東富士演習場", region="静岡",
                      coordinate="北緯 35.2690  東経 138.8200", image="/static/images/higashifuji.jpg")

        section_header("LATEST WEATHER", "最新の気象情報")
        weather_card()

        section_header("ATMOSPHERIC PROFILE", "高度別の気象データ")
        altitude_weather_card()

    floating_nav("home")


def location_card(
    eyebrow: str, title: str, region: str, coordinate: str, image: str, recent: bool = False
):
    with ui.card().classes("w-full location-card"):
        ui.image(image).classes("location-card-image")
        ui.element("div").classes("location-card-fade")
        ui.element("div").classes("location-card-hud")

        with ui.column().classes("location-card-content"):
            with ui.row().classes("items-start justify-between w-full"):
                with ui.column().classes("gap-0"):
                    ui.label(eyebrow).classes("location-eyebrow")
                    ui.label(title).classes("location-title")
                    ui.label(region).classes("location-region")

            if recent:
                ui.label("RECENT").classes("location-recent-badge")

            with ui.row().classes("location-coordinate-row"):
                ui.icon("gps_fixed").classes("location-coordinate-icon")
                with ui.column().classes("gap-0"):
                    ui.label(coordinate).classes("location-coordinate")

            ui.button("現在地を取得", icon="my_location", on_click=None).props("flat no-caps").classes(
                "location-gps-button"
            )


def section_header(eyebrow: str, title: str):
    with ui.column().classes("dashboard-section-header"):
        ui.label(eyebrow).classes("dashboard-section-eyebrow")
        ui.label(title).classes("dashboard-section-title")
        ui.element("div").classes("dashboard-section-line")


def weather_card():
    with ui.card().classes("w-full weather-card"):
        # Header
        with ui.row().classes("altitude-card-header"):
            with ui.column().classes("gap-0"):
                ui.label("LATEST WEATHER").classes("altitude-eyebrow")
                ui.label("矢臼別演習場").classes("altitude-title")

            ui.icon("cloud").classes("altitude-icon")

        # Divider
        ui.element("div").classes("weather-divider")

        # Metrics
        with ui.row().classes("weather-metrics"):
            weather_metric("25.4", "°C", "TEMPERATURE")
            weather_metric("4.8", "m/s", "WIND")
            weather_metric("76", "%", "HUMIDITY")

        # Footer
        with ui.row().classes("weather-footer"):
            ui.label("FNL / Latest available data").classes("weather-source")
            ui.button("最新データを取得", icon="refresh", on_click=dialog_latest_weather).props(
                "unelevated no-caps"
            ).classes("weather-refresh-button")

def weather_metric(value: str, unit: str, label: str):
    with ui.column().classes("weather-metric"):
        with ui.row().classes("items-baseline gap-1"):
            ui.label(value).classes("weather-metric-value")
            ui.label(unit).classes("weather-metric-unit")
        ui.label(label).classes("weather-metric-label")

def altitude_weather_card():
    with ui.card().classes("w-full altitude-card"):

        # Header
        with ui.row().classes("altitude-card-header"):
            with ui.column().classes("gap-0"):
                ui.label("ATMOSPHERIC PROFILE").classes("altitude-eyebrow")
                ui.label("高度別の気象データ").classes("altitude-title")

            ui.icon("analytics").classes("altitude-icon")

        ui.label("高度を選択して気象状態を確認できます。").classes("altitude-description")

        # Altitude selector
        with ui.row().classes("altitude-selector-row"):
            with ui.column().classes("altitude-selector"):
                ui.label("ALTITUDE").classes("altitude-selector-label")
                ui.select([0, 500, 1000, 1500, 2000, 3000, 5000], value=1000).props(
                    "outlined dense"
                ).classes("w-full")

            ui.label("m").classes("altitude-unit")

        # Action
        ui.button("気象データを表示", icon="analytics").props("unelevated no-caps").classes(
            "altitude-action-button"
        )

def table_page():
    with ui.column().classes("page-content"):
        page_header("LOCATIONS", "演習場一覧")

        domestic_rows = [
            {"code": "Y", "loc": "矢臼別演習場", "lat": 43.2997, "lon": 144.9873},
            {"code": "K", "loc": "上富良野演習場", "lat": 43.4230, "lon": 142.4800},
            {"code": "I", "loc": "岩手山演習場", "lat": 39.8650, "lon": 140.9730},
            {"code": "O", "loc": "王城寺原演習場", "lat": 38.5710, "lon": 140.8610},
            {"code": "E", "loc": "東富士演習場", "lat": 35.2947, "lon": 138.8536},
            {"code": "N", "loc": "北富士演習場", "lat": 35.4500, "lon": 138.8000},
            {"code": "A", "loc": "饗庭野演習場", "lat": 35.3460, "lon": 136.0390},
            {"code": "H", "loc": "日出生台演習場", "lat": 33.2860, "lon": 131.3990},
            {"code": "S", "loc": "防衛装備庁下北試験場", "lat": 41.3050, "lon": 141.3070},
        ]

        overseas_rows = [
            {"code": "YPG", "loc": "Yuma Proving Ground", "country": "USA", "lat": 32.8600, "lon": -114.4000},
            {"code": "KOF", "loc": "Kofa Range", "country": "USA", "lat": 33.0000, "lon": -114.0000},
        ]

        def create_range_table(rows, overseas=False):
            columns = [
                {"name": "loc", "label": "場所", "field": "loc", "align": "left"},
                {"name": "menu", "label": "", "field": "menu", "style": "width: 48px", "align": "center"},
            ]
            table = ui.table(columns=columns, rows=rows, row_key="code").props(
                "flat bordered hide-header"
            ).classes("w-full glass-table")

            async def row_clicked(e):
                await dialog_latest_weather()

            def open_map(row):
                ui.navigate.to(f'/map/{row["lat"]}/{row["lon"]}')

            table.on("row-click", row_clicked)

            with table.add_slot("body-cell-loc", r'''
                <q-td :props="props" class="range-table-location">
                    <div class="range-row-content">
                        <div class="range-name">{{ props.row.loc }}</div>
                        <div v-if="props.row.country" class="range-country">{{ props.row.country }}</div>
                        <div class="range-coordinates">
                            <span>北緯 {{ props.row.lat.toFixed(4) }}</span>
                            <span>東経 {{ props.row.lon.toFixed(4) }}</span>
                        </div>
                    </div>
                </q-td>
            '''):
                pass

            with table.add_slot("body-cell-menu", r'''
                <q-td :props="props" auto-width class="range-menu-cell">
                    <q-btn flat round dense icon="more_vert" class="range-menu-button"
                        @click.stop="$parent.$emit('menu-click', props.row)">
                        <q-menu class="glass-menu" :offset="[0, -24]">
                            <q-list style="min-width: 180px">
                                <q-item clickable v-close-popup
                                    @click="$parent.$emit('map-click', props.row)">
                                    <q-item-section avatar><q-icon name="map"/></q-item-section>
                                    <q-item-section>地図を表示</q-item-section>
                                </q-item>
                                <q-item clickable v-close-popup
                                    @click="$parent.$emit('detail-click', props.row)">
                                    <q-item-section avatar><q-icon name="info"/></q-item-section>
                                    <q-item-section>詳細</q-item-section>
                                </q-item>
                                <q-item clickable v-close-popup
                                    @click="$parent.$emit('favorite-click', props.row)">
                                    <q-item-section avatar><q-icon name="star"/></q-item-section>
                                    <q-item-section>お気に入り</q-item-section>
                                </q-item>
                            </q-list>
                        </q-menu>
                    </q-btn>
                </q-td>
            '''):
                pass

            table.on("map-click", lambda e: open_map(e.args))
            table.on("menu-click", None)
            table.on("detail-click", lambda e: ui.notify(f'詳細: {e.args["loc"]}', position="top"))
            table.on("favorite-click", lambda e: ui.notify(f'お気に入り: {e.args["loc"]}', position="top"))
            return table

        for title, subtitle, rows in [
            ("DOMESTIC", "国内射場", domestic_rows),
            ("OVERSEAS", "国外射場", overseas_rows),
        ]:
            with ui.column().classes("range-section"):
                with ui.row().classes("range-section-title"):
                    ui.label(title)
                    ui.label(subtitle)
                create_range_table(rows)

    floating_nav("table")

MAP_TILES = {
    "standard": {
        "url": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        "options": {
            "maxZoom": 19,
            "attribution": "&copy; OpenStreetMap contributors",
        },
    },
    "satellite": {
        "url": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        "options": {
            "maxZoom": 19,
            "attribution": "Tiles &copy; Esri",
        },
    },
    "terrain": {
        "url": "https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png",
        "options": {
            "maxZoom": 17,
            "attribution": (
                "&copy; OpenStreetMap contributors, "
                "&copy; OpenTopoMap"
            ),
        },
    },
}

def set_map_type(map_element, map_type: str):
    tile = MAP_TILES[map_type]

    map_element.clear_layers()
    map_element.tile_layer(
        url_template=tile["url"],
        options=tile["options"],
    )

def map_page(lat: float, lon: float):
    with ui.element("div").classes("map-page"):

        map_element = ui.leaflet(center=(lat, lon), zoom=10).classes("map-view")
        set_map_type(map_element, get_setting("map_type"))

        # Floating Back Button
        with ui.element("div").classes("map-back-button"):
            ui.button(icon="arrow_back", on_click=lambda: ui.navigate.back()).props("flat round")

        # Current Location Overlay
        with ui.element("div").classes("map-overlay"):
            ui.label("CURRENT LOCATION").classes("map-overlay-label")
            ui.label(f"{lat:.4f}, {lon:.4f}").classes("map-overlay-coordinate")

        # Location Information
        with ui.card().classes("map-info-card"):
            with ui.row().classes("map-info-header"):
                ui.icon("location_on").classes("map-location-icon")

                with ui.column().classes("gap-0"):
                    ui.label("LOCATION").classes("map-info-eyebrow")
                    ui.label("表示地点").classes("map-info-title")

            ui.separator().classes("map-info-separator")

            with ui.row().classes("map-coordinate-row"):
                with ui.column().classes("map-coordinate-item"):
                    ui.label("LATITUDE").classes("map-coordinate-label")
                    ui.label(f"{lat:.4f}°").classes("map-coordinate-value")

                with ui.column().classes("map-coordinate-item"):
                    ui.label("LONGITUDE").classes("map-coordinate-label")
                    ui.label(f"{lon:.4f}°").classes("map-coordinate-value")


def apply_map_type():
    set_map_type(map_element, get_setting("map_type"))

# =========================================================
# Settings Definition
# =========================================================

SETTINGS = {
    "appearance": {
        "icon": "dark_mode",
        "title": "外観",
        "options": {
            "system": "システム設定に従う",
            "light": "ライト",
            "dark": "ダーク",
            "olive":"オリーブドラブ",
            "olive_dark": "オリーブドラブ (濃)"
        },
        "default": "system",
        "on_change": "apply_appearance",
    },
    "unit": {
        "icon": "straighten",
        "title": "単位系*",
        "options": {"metric": "Metric", "imperial": "Imperial"},
        "default": "metric",
    },
    "weather_source": {
        "icon": "cloud",
        "title": "データソース*",
        "options": {"fnl": "FNL"},
        "default": "fnl",
    },
    "weather_update": {
        "icon": "update",
        "title": "更新間隔*",
        "options": {
            "auto": "自動",
            "1h": "1時間",
            "3h": "3時間",
            "6h": "6時間",
        },
        "default": "auto",
    },
    "map_type": {
        "icon": "map",
        "title": "地図の種類",
        "options": {
            "standard": "デフォルト",
            "satellite": "航空写真",
            "terrain": "地形",
        },
        "default": "standard",
    },
    "map_zoom": {
        "icon": "zoom_in",
        "title": "初期ズーム*",
        "options": {"8": "8", "10": "10", "12": "12", "14": "14"},
        "default": "10",
    },
    "domestic_locations": {
        "icon": "flag",
        "title": "国内射場",
        "options": {},
        "default": None,
        "right_arrow": False,
        "value": "9ヶ所",
    },
    "foreign_locations": {
        "icon": "public",
        "title": "国外射場",
        "options": {},
        "default": None,
        "right_arrow": False,
        "value": "2ヶ所",
    },
    "favorites": {
        "icon": "star",
        "title": "お気に入り*",
        "options": {},
        "default": None,
        "right_arrow": True,
        "value": "管理",
    },
    "notifications": {
        "icon": "notifications",
        "title": "通知*",
        "options": {"enabled": "有効", "disabled": "無効"},
        "default": "enabled",
    },
    "version": {
        "icon": "info",
        "title": "バージョン",
        "options": {},
        "default": None,
        "right_arrow": False,
        "value": "0.0.1-alpha",
    },
}

# =========================================================
# Storage
# =========================================================

def get_setting(key: str):
    setting = SETTINGS[key]

    # 固定表示項目
    if not setting["options"]:
        return setting.get("value", "")

    if key not in app.storage.user:
        app.storage.user[key] = setting["default"]

    return app.storage.user[key]


def set_setting(key: str, value: str):
    app.storage.user[key] = value


def get_setting_label(key: str):
    setting = SETTINGS[key]
    value = get_setting(key)

    # 固定表示項目
    if not setting["options"]:
        return value

    return setting["options"].get(value, value)

def apply_setting(key: str, value: str):
    handler_name = SETTINGS[key].get("on_change")

    if handler_name:
        handler = globals().get(handler_name)

        if handler:
            handler(value)

# =========================================================
# Setting Dialog
# =========================================================

def open_setting_dialog(key: str, on_changed=None):
    setting = SETTINGS[key]

    # 選択肢がない項目はダイアログを開かない
    if not setting["options"]:
        return

    current = get_setting(key)

    with ui.dialog() as dialog:
        with ui.card().classes("setting-dialog"):
            # Header
            with ui.row().classes("setting-dialog-header"):
                ui.label(setting["title"]).classes("setting-dialog-title")
                ui.button(icon="close", on_click=dialog.close).props("flat round dense")

            # Options
            with ui.column().classes("setting-options"):
                for value, label in setting["options"].items():

                    def select(value=value):
                        set_setting(key, value)
                        apply_setting(key, value)

                        if on_changed:
                            on_changed()

                        dialog.close()

                    with ui.element("div").classes("setting-option").on("click", select):
                        ui.label(label).classes("setting-option-label")

                        check = ui.icon("check").classes("setting-option-check")
                        check.set_visibility(value == current)

    dialog.open()

# =========================================================
# Settings Table
# =========================================================

def settings_table(keys):
    rows = [
        {
            "key": key,
            "icon": SETTINGS[key]["icon"],
            "title": SETTINGS[key]["title"],
            "value": get_setting_label(key),
            "right_arrow": SETTINGS[key].get("right_arrow", True),
        }
        for key in keys
    ]

    columns = [
        {"name": "title", "label": "", "field": "title", "align": "left"},
        {"name": "value", "label": "", "field": "value", "align": "right"},
    ]

    table = ui.table(columns=columns, rows=rows, row_key="key").classes("settings-table")

    # Row
    table.add_slot(
        "body",
        r"""
        <q-tr :props="props" class="settings-table-row"
              @click="$parent.$emit('row-click', props.row)">

            <!-- Left -->
            <q-td key="title" :props="props" class="settings-table-title-cell">
                <div class="settings-table-title">
                    <q-icon :name="props.row.icon" class="settings-table-icon" />
                    <span>{{ props.row.title }}</span>
                </div>
            </q-td>

            <!-- Right -->
            <q-td key="value" :props="props" class="settings-table-value-cell">
                <div class="settings-table-value">
                    <span>{{ props.row.value }}</span>
                    <q-icon v-if="props.row.right_arrow" name="chevron_right"
                            class="settings-table-arrow" />
                </div>
            </q-td>

        </q-tr>
        """,
    )

    # Update table
    def refresh():
        for row in rows:
            row["value"] = get_setting_label(row["key"])

        table.update_rows(rows)

    # Row click
    def handle_row_click(e):
        key = e.args["key"]
        open_setting_dialog(key, on_changed=refresh)

    table.on("row-click", handle_row_click)

    return table

# =========================================================
# Settings Section
# =========================================================

def settings_section(eyebrow: str, title: str, keys: list[str]):
    with ui.column().classes("settings-section"):
        with ui.row().classes("settings-section-header"):
            ui.label(eyebrow).classes("settings-section-eyebrow")
            ui.label(title).classes("settings-section-title")

        with ui.element("div").classes("settings-card"):
            settings_table(keys)


def settings_page():
    with ui.column().classes("page-content settings-page"):
        page_header("SETTINGS", "設定")
        ui.label("*は現在未実装")
        settings_section("GENERAL", "一般", ["appearance", "unit"])
        settings_section("WEATHER", "気象情報", ["weather_source", "weather_update"])
        settings_section("MAP", "地図", ["map_type", "map_zoom"])
        settings_section(
            "LOCATIONS", "演習場", ["domestic_locations", "foreign_locations", "favorites"],
        )
        settings_section("APP", "アプリ", ["notifications", "version"])

        # Floating Navigation と重ならないように
        ui.element("div").style("height: calc(110px + env(safe-area-inset-bottom));")

    floating_nav("settings")

# =========================================================
# Appearance
# =========================================================

BODY_CLASSES = [
    "theme-default",
    "theme-olive",
    "theme-olive-dark",
]

dark = ui.dark_mode()

def apply_appearance(value: str):
    # bodyクラスをリセット
    ui.query("body").classes(remove=" ".join(BODY_CLASSES))
    ui.colors(**UI_COLORS[value])

    match value:
        case "system":
            dark.auto()
            ui.query("body").classes(add="theme-default")

        case "light":
            dark.disable()
            ui.query("body").classes(add="theme-default")

        case "dark":
            dark.enable()
            ui.query("body").classes(add="theme-default")

        case "olive":
            dark.enable()
            ui.query("body").classes(add="theme-olive")

        case "olive_dark":
            dark.enable()
            ui.query("body").classes(add="theme-olive-dark")

theme = app.storage.user.get("appearance", "system")
apply_appearance(theme)

# PWA化
app.add_static_files("/static", "static")

add_head()

ui.sub_pages({
    "/": home_page,
    "/table": table_page,
    "/map/{lat}/{lon}": map_page,
    "/settings": settings_page,
}).classes("w-full")

port = int(os.environ.get("PORT", 8080))

ui.run(
    host="0.0.0.0",
    port=port,
    storage_secret="6d2740f2fcfc818d68a39f9d6654db89718db917f1b872e4545cf7c9b91f72e3",
)
