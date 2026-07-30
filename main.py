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
    with ui.column().classes("page-content"):
        page_header("OVERVIEW", "ホーム")
        ui.label("PROTOTYPE UI: overall layout may be altered")

        ui.label("直近に使用した演習場").classes("text-subtitle1 q-mt-md")

        with ui.card().classes("w-full location-card"):
            ui.image("/static/images/yausubetsu.jpg").classes("location-card-image")  # 背景写真
            ui.element("div").classes("location-card-fade")  # 左側の白いフェード
            ui.element("div").classes("location-card-hud")  # 薄いHUDエフェクト

            with ui.column().classes("location-card-content"):  # コンテンツ
                with ui.row().classes("items-start justify-between w-full"):  # 上部
                    with ui.column().classes("gap-0"):
                        ui.label("YAUSUBETSU TRAINING AREA").classes("location-eyebrow")
                        ui.label("矢臼別演習場").classes("location-title")
                        ui.label("北海道").classes("location-region")

                with ui.row().classes("location-coordinate-row"):  # 座標
                    ui.icon("gps_fixed").classes("location-coordinate-icon")

                    with ui.column().classes("gap-0"):
                        ui.label("北緯 43.2997 東経 144.9873").classes("location-coordinate")

                ui.button("現在地を取得", icon="my_location", on_click=None,
                ).props("flat").classes("location-gps-button")  # 下部ボタン

        ui.label("最新の気象情報").classes("text-subtitle1 q-mt-lg")

        with ui.card().classes("w-full"):

            with ui.row().classes("items-center justify-between w-full"):
                with ui.column().classes("gap-0"):
                    ui.label("○○演習場").classes("text-h6")
                    ui.label("最新データ").classes("text-caption text-grey-6")

                ui.icon("sunny").classes("text-3xl text-grey-6")

            ui.separator().classes("q-my-sm")

            with ui.row().classes("w-full"):

                with ui.column().classes("flex-1 items-center"):
                    ui.label("気温").classes("text-caption text-grey-6")
                    ui.label("25.4 °C").classes("text-body1")

                with ui.column().classes("flex-1 items-center"):
                    ui.label("風速").classes("text-caption text-grey-6")
                    ui.label("4.8 m/s").classes("text-body1")

                with ui.column().classes("flex-1 items-center"):
                    ui.label("湿度").classes("text-caption text-grey-6")
                    ui.label("76 %").classes("text-body1")

            ui.button("最新データを取得", icon="refresh", on_click=dialog_latest_weather,
            ).props("unelevated").classes("w-full q-mt-md")

        ui.label("高度別の気象データ").classes("text-subtitle1 q-mt-lg")

        with ui.card().classes("w-full"):

            ui.label("高度を選択して気象状態を確認できます。").classes("text-body2")

            with ui.row().classes("items-center w-full q-mt-sm"):

                ui.select(
                    [0, 500, 1000, 1500, 2000, 3000, 5000], value=1000, label="高度",
                ).classes("flex-1")

                ui.label("m").classes("q-ml-sm")

            ui.button("気象データを表示", icon="analytics").props("flat").classes("w-full q-mt-sm")

    floating_nav("home")


def table_page():
    with ui.column().classes("page-content"):
        page_header("LOCATIONS", "演習場一覧")

        # =========================================================
        # 国内射場
        # =========================================================
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

        # =========================================================
        # 国外射場
        # ※ 実際に使用する場所に置き換えてください
        # =========================================================
        overseas_rows = [
            {
                "code": "YPG",
                "loc": "Yuma Proving Ground",
                "country": "USA",
                "lat": 32.8600,
                "lon": -114.4000,
            },
            {
                "code": "KOF",
                "loc": "Kofa Range",
                "country": "USA",
                "lat": 33.0000,
                "lon": -114.0000,
            },
        ]

        # =========================================================
        # 共通テーブル生成
        # =========================================================
        def create_range_table(rows, overseas=False):

            columns = [
                {
                    "name": "loc",
                    "label": "場所",
                    "field": "loc",
                    "align": "left",
                },
                {
                    "name": "menu",
                    "label": "",
                    "field": "menu",
                    "style": "width: 48px",
                    "align": "center",
                },
            ]

            table = ui.table(
                columns=columns,
                rows=rows,
                row_key="code",
            ).props(
                "flat bordered hide-header"
            ).classes(
                "w-full glass-table"
            )

            async def row_clicked(e):
                await dialog_latest_weather()

            def open_map(row):
                ui.navigate.to(
                    f'/map/{row["lat"]}/{row["lon"]}'
                )

            table.on("row-click", row_clicked)

            # -----------------------------------------------------
            # 場所名 + 国名 + 緯度経度
            # -----------------------------------------------------
            with table.add_slot("body-cell-loc", r'''
                <q-td
                    :props="props"
                    class="range-table-location"
                >
                    <div class="range-row-content">

                        <div class="range-name">
                            {{ props.row.loc }}
                        </div>

                        <div
                            v-if="props.row.country"
                            class="range-country"
                        >
                            {{ props.row.country }}
                        </div>

                        <div class="range-coordinates">
                            <span>
                                北緯 {{ props.row.lat.toFixed(4) }}
                            </span>

                            <span>
                                東経 {{ props.row.lon.toFixed(4) }}
                            </span>
                        </div>

                    </div>
                </q-td>
            '''):
                pass

            # -----------------------------------------------------
            # メニュー
            # -----------------------------------------------------
            with table.add_slot("body-cell-menu", r'''
                <q-td
                    :props="props"
                    auto-width
                    class="range-menu-cell"
                >
                    <q-btn
                        flat
                        round
                        dense
                        icon="more_vert"
                        class="range-menu-button"
                        @click.stop="$parent.$emit(
                            'menu-click',
                            props.row
                        )"
                    >

                        <q-menu
                            class="glass-menu"
                            :offset="[0, -24]"
                        >
                            <q-list style="min-width: 180px">

                                <q-item
                                    clickable
                                    v-close-popup
                                    @click="$parent.$emit(
                                        'map-click',
                                        props.row
                                    )"
                                >
                                    <q-item-section avatar>
                                        <q-icon name="map"/>
                                    </q-item-section>

                                    <q-item-section>
                                        地図を表示
                                    </q-item-section>
                                </q-item>

                                <q-item
                                    clickable
                                    v-close-popup
                                    @click="$parent.$emit(
                                        'detail-click',
                                        props.row
                                    )"
                                >
                                    <q-item-section avatar>
                                        <q-icon name="info"/>
                                    </q-item-section>

                                    <q-item-section>
                                        詳細
                                    </q-item-section>
                                </q-item>

                                <q-item
                                    clickable
                                    v-close-popup
                                    @click="$parent.$emit(
                                        'favorite-click',
                                        props.row
                                    )"
                                >
                                    <q-item-section avatar>
                                        <q-icon name="star"/>
                                    </q-item-section>

                                    <q-item-section>
                                        お気に入り
                                    </q-item-section>
                                </q-item>

                            </q-list>
                        </q-menu>

                    </q-btn>
                </q-td>
            '''):
                pass

            table.on(
                "map-click",
                lambda e: open_map(e.args)
            )

            table.on("menu-click", None)

            table.on(
                "detail-click",
                lambda e: ui.notify(
                    f'詳細: {e.args["loc"]}',
                    position="top"
                )
            )

            table.on(
                "favorite-click",
                lambda e: ui.notify(
                    f'お気に入り: {e.args["loc"]}',
                    position="top"
                )
            )

            return table

        # =========================================================
        # 国内
        # =========================================================
        with ui.column().classes("range-section"):
            with ui.row().classes("range-section-title"):
                ui.label("DOMESTIC")
                ui.label("国内射場")

            create_range_table(domestic_rows)

        # =========================================================
        # 国外
        # =========================================================
        with ui.column().classes("range-section"):
            with ui.row().classes("range-section-title"):
                ui.label("OVERSEAS")
                ui.label("国外射場")

            create_range_table(
                overseas_rows,
                overseas=True,
            )

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
    with ui.column().classes("page-content map-page"):

        page_header("MAP", "地図")

        with ui.element("div").classes("map-wrapper"):
            map_element = ui.leaflet(center=(lat, lon),zoom=10).classes("map-view")
            set_map_type(map_element, get_setting("map_type"))

            # 地図上の情報
            with ui.element("div").classes("map-overlay"):
                ui.label("CURRENT LOCATION").classes("map-overlay-label")
                ui.label( f"{lat:.4f}, {lon:.4f}").classes( "map-overlay-coordinate")

        # ---------------------------------------------------------
        # Location information
        # ---------------------------------------------------------
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
                    ui.label( f"{lat:.4f}°").classes("map-coordinate-value")
                with ui.column().classes("map-coordinate-item"):
                    ui.label("LONGITUDE").classes("map-coordinate-label")
                    ui.label(f"{lon:.4f}°").classes("map-coordinate-value")

        # floating navigationとの重なり防止
        ui.element("div").classes("map-bottom-space")

    floating_nav("table")


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
            "satellite": "航空写真e",
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


def settings_item(key: str):
    setting = SETTINGS[key]

    with ui.element("div").classes("settings-item") as item:
        # Left
        with ui.element("div").classes("settings-item-left"):
            ui.icon(setting["icon"]).classes("settings-item-icon")
            ui.label(setting["title"]).classes("settings-item-title")

        # Right
        with ui.element("div").classes("settings-item-right"):
            ui.label(get_setting_label(key)).classes("settings-item-value")

            if setting.get("right_arrow", True):
                ui.icon("chevron_right").classes("settings-item-arrow")

        if setting["options"]:
            item.on("click", lambda: open_setting_dialog(key))



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
