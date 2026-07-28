from nicegui import app, ui
import sys
import os
from urllib.request import build_opener
# import pygrib


def downloader():
    opener = build_opener()
    file = "https://osdf-director.osg-htc.org/ncar/gdex/d083002/grib2/2026/2026.07/fnl_20260727_00_00.grib2"
    ofile = os.path.basename(file)
    sys.stdout.write("downloading " + ofile + " ... ")
    sys.stdout.flush()
    infile = opener.open(file)
    outfile = open(ofile, "wb")
    outfile.write(infile.read())
    outfile.close()
    sys.stdout.write("done\n")


def grib_loader():
    pass
    # grbs = pygrib.open("2026.07/fnl_20260727_00_00.grib2")
    # grbs.read()


def table_page():
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
    for row in rows:
        row["latlon"] = f'{row["lat"]:.1f}\n{row["lon"]:.1f}'
    columns = [
        {"name": "code", "label": "コード", "field": "code",
            "style": "width:60px", "align": "left"},
        {"name": "loc", "label": "場所", "field": "loc", "align": "left"},
        {"name": "latlon", "label": "緯度経度", "field": "latlon",
            "style": "width:70px", "align": "left"},
        {"name": "map", "label": "", "field": "map",
            "style": "width:48px", "align": "left"},
    ]

    def row_clicked(e):
        row = e.args[1]
        ui.notify(f'選択: {row["loc"]}')
        # ここに行タップ時の処理を書く

    def open_map(row):
        ui.navigate.to(f'/map/{row["lat"]}/{row["lon"]}')

    table = ui.table(columns=columns, rows=rows,
                     row_key="code").props("flat bordered").classes("w-full")
    table.on("row-click", row_clicked)

    with table.add_slot('body-cell-latlon', r'''
        <q-td :props="props" style="white-space: pre-line;">
        {{ props.value }}
        </q-td>
        '''):
        pass

    with table.add_slot("body-cell-map", r"""
        <q-td :props="props">
            <q-btn flat round dense icon="map" color="primary"
            @click.stop="$parent.$emit('map-click', props.row)"
            />
        </q-td>
        """):
        pass

    table.on("map-click", lambda e: open_map(e.args))
    floating_nav("table")


def map_page(lat: float, lon: float):
    ui.leaflet(center=(lat, lon), zoom=10).classes("w-full").style("height: 85vh;")
    floating_nav("table")


def settings_page():
    ui.label("設定").classes("text-h5")

    def change_theme(e):
        app.storage.user[DISPLAY_THEME_KEY] = e.value
        apply_display_theme(e.value)

    with ui.column().classes("w-full gap-3"):

        with ui.row().classes("w-full items-center"):
            ui.label("表示テーマ").classes("w-40")
            ui.select(
                options=DISPLAY_THEMES,
                value=app.storage.user.get(DISPLAY_THEME_KEY, "system"),
                on_change=change_theme,
            ).props("outlined dense").classes("flex-1")

    floating_nav("settings")


def floating_nav(current: str):
    tabs = [
        ("table_chart", "一覧", "/", "table"),
        ("settings", "設定", "/settings", "settings"),
    ]

    with ui.element("div").classes("floating-nav"):

        for icon, label, path, name in tabs:

            active = (current == name)

            ui.button(
                label if active else "",
                icon=icon,
                on_click=lambda p=path: ui.navigate.to(p),
            ).props(
                "unelevated no-caps rounded" if active else "flat round"
            ).style(f"""
                width: {'120px' if active else '48px'};
                height:48px;
                border-radius:999px;

                transition:

                    all .25s cubic-bezier(.2,.8,.2,1);

                {'background:rgba(255,255,255,.35);' if active else ''}
            """)


DISPLAY_THEME_KEY = "display_theme"

DISPLAY_THEMES = {
    "system":       "システム設定",
    "light":        "ライト",
    "dark":         "ダーク",
    "olive":        "オリーブドラブ",
    "olive_dark":   "オリーブドラブ（ダーク）",
    "jsdf":         "陸上自衛隊迷彩",
}

dark = ui.dark_mode()

BODY_CLASSES = [
    "theme-default",
    "theme-olive",
    "theme-olive-dark",
    "theme-jsdf",
]


def apply_display_theme(theme: str):

    # bodyクラスをリセット
    ui.query("body").classes(remove=" ".join(BODY_CLASSES))

    match theme:

        # -------------------------
        case "system":

            dark.auto()

            ui.colors(
                primary="#1976D2",
                secondary="#42A5F5",
                accent="#2196F3",
            )

            ui.query("body").classes(add="theme-default")

        # -------------------------
        case "light":

            dark.disable()

            ui.colors(
                primary="#1976D2",
                secondary="#42A5F5",
                accent="#2196F3",
            )

            ui.query("body").classes(add="theme-default")

        # -------------------------
        case "dark":

            dark.enable()

            ui.colors(
                primary="#64B5F6",
                secondary="#42A5F5",
                accent="#90CAF9",
            )

            ui.query("body").classes(add="theme-default")

        # -------------------------
        case "olive":

            dark.enable()

            ui.colors(
                primary="#687A34",
                secondary="#81944A",
                accent="#A3B96A",
            )

            ui.query("body").classes(add="theme-olive")

        # -------------------------
        case "olive_dark":

            dark.enable()

            ui.colors(
                primary="#80944A",
                secondary="#94AA58",
                accent="#B5CC77",
            )

            ui.query("body").classes(add="theme-olive-dark")

        # -------------------------
        case "jsdf":

            dark.enable()

            ui.colors(
                primary="#78864A",
                secondary="#A29363",
                accent="#C9B979",
            )

            ui.query("body").classes(add="theme-jsdf")


theme = app.storage.user.get(DISPLAY_THEME_KEY, "system")

apply_display_theme(theme)

# PWA化
app.add_static_files("/static", "static")

ui.add_head_html("""
    <link rel="stylesheet" href="/static/css/theme.css">
    <link rel="manifest" href="/static/manifest.json">
    <script>
    if ("serviceWorker" in navigator) {
        navigator.serviceWorker.register("/static/sw.js");
    }
    </script>
""")

ui.sub_pages({
    "/": table_page,
    "/map/{lat}/{lon}": map_page,
    "/settings": settings_page,
}).classes("w-full")

port = int(os.environ.get("PORT", 8080))

ui.run(
    host="0.0.0.0",
    port=port,
    storage_secret="6d2740f2fcfc818d68a39f9d6654db89718db917f1b872e4545cf7c9b91f72e3",
)
