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

        rows = [
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
                "style": "width:48px",
                "align": "center",
            },
        ]

        async def row_clicked(e):
            await dialog_latest_weather()

        def open_map(row):
            ui.navigate.to(f'/map/{row["lat"]}/{row["lon"]}')

        table = ui.table(
            columns=columns,
            rows=rows,
            row_key="code",
        ).props("flat bordered hide-header").classes("w-full glass-table")

        table.on("row-click", row_clicked)

        # 場所名 + 緯度経度
        with table.add_slot('body-cell-loc', r'''
            <q-td :props="props" style="padding-top: 12px; padding-bottom: 12px;">
                <div class="column items-start">
                    <div class="text-body1">
                        {{ props.row.loc }}
                    </div>
                    <div
                        class="text-caption"
                        style="
                            display: flex;
                            gap: 12px;
                            opacity: 0.55;
                            font-size: 11px;
                        "
                    >
                        <span>北緯 {{ props.row.lat.toFixed(4) }}</span>
                        <span>東経 {{ props.row.lon.toFixed(4) }}</span>
                    </div>
                </div>
            </q-td>
        '''):
            pass

        with table.add_slot('body-cell-menu', r'''
            <q-td :props="props" auto-width>
                <q-btn
                    flat
                    round
                    dense
                    icon="more_vert"
                    @click.stop="$parent.$emit('menu-click', props.row)"
                >
                    <q-menu class="glass-menu" :offset="[0, -24]">
                        <q-list style="min-width:180px">

                            <q-item
                                clickable
                                v-close-popup
                                @click="$parent.$emit('map-click', props.row)"
                            >
                                <q-item-section avatar>
                                    <q-icon name="map"/>
                                </q-item-section>
                                <q-item-section>地図を表示</q-item-section>
                            </q-item>

                            <q-item
                                clickable
                                v-close-popup
                                @click="$parent.$emit('detail-click', props.row)"
                            >
                                <q-item-section avatar>
                                    <q-icon name="info"/>
                                </q-item-section>
                                <q-item-section>詳細</q-item-section>
                            </q-item>

                            <q-item
                                clickable
                                v-close-popup
                                @click="$parent.$emit('favorite-click', props.row)"
                            >
                                <q-item-section avatar>
                                    <q-icon name="star"/>
                                </q-item-section>
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
        table.on(
            "detail-click",
            lambda e: ui.notify(f'詳細: {e.args["loc"]}', position="top")
        )
        table.on(
            "favorite-click",
            lambda e: ui.notify(f'お気に入り: {e.args["loc"]}', position="top")
        )

    floating_nav("table")


def map_page(lat: float, lon: float):
    ui.leaflet(center=(lat, lon), zoom=10).classes("w-full").style("height: 85vh;")
    floating_nav("table")


def settings_page():
    with ui.column().classes("page-content"):
        page_header("SYSTEM", "設定")

        def change_theme(e):
            app.storage.user[DISPLAY_THEME_KEY] = e.value
            apply_display_theme(e.value)

        with ui.column():

            with ui.row().classes("w-full items-center"):
                ui.label("表示テーマ").classes("w-25")
                ui.select(
                    options=DISPLAY_THEMES,
                    value=app.storage.user.get(DISPLAY_THEME_KEY, "system"),
                    on_change=change_theme,
                ).props('outlined dense behavior="menu"')

            with ui.row().classes("w-full items-center"):
                ui.label("表示単位").classes("w-25")
                ui.select(
                    options=["m/s", "kt"],
                    value="m/s",
                ).props('outlined dense behavior="menu"')
    floating_nav("settings")


DISPLAY_THEME_KEY = "display_theme"

DISPLAY_THEMES = {
    "system": "システム設定",
    "light": "ライト",
    "dark": "ダーク",
    "olive": "オリーブドラブ",
    "olive_dark": "オリーブドラブ (濃)",
}

BODY_CLASSES = [
    "theme-default",
    "theme-olive",
    "theme-olive-dark",
]

dark = ui.dark_mode()

def apply_display_theme(theme: str):
    # bodyクラスをリセット
    ui.query("body").classes(remove=" ".join(BODY_CLASSES))
    ui.colors(**UI_COLORS[theme])

    match theme:
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


theme = app.storage.user.get(DISPLAY_THEME_KEY, "system")
apply_display_theme(theme)

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
