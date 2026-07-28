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
        {"コード": "Y", "名称": "矢臼別演習場", "緯度": 43.2997, "経度": 144.9873},
        {"コード": "K", "名称": "上富良野演習場", "緯度": 43.4230, "経度": 142.4800},
        {"コード": "I", "名称": "岩手山演習場", "緯度": 39.8650, "経度": 140.9730},
        {"コード": "O", "名称": "王城寺原演習場", "緯度": 38.5710, "経度": 140.8610},
        {"コード": "E", "名称": "東富士演習場", "緯度": 35.2947, "経度": 138.8536},
        {"コード": "N", "名称": "北富士演習場", "緯度": 35.4500, "経度": 138.8000},
        {"コード": "A", "名称": "饗庭野演習場", "緯度": 35.3460, "経度": 136.0390},
        {"コード": "H", "名称": "日出生台演習場", "緯度": 33.2860, "経度": 131.3990},
        {"コード": "S", "名称": "防衛装備庁下北試験場", "緯度": 41.3050, "経度": 141.3070},
    ]
    columns = [
        {"name": "コード", "label": "コード", "field": "コード"},
        {"name": "名称", "label": "名称", "field": "名称"},
        {"name": "緯度", "label": "緯度", "field": "緯度"},
        {"name": "経度", "label": "経度", "field": "経度"},
        {"name": "map", "label": "", "field": "map"},
    ]

    def row_clicked(e):
        row = e.args[1]
        ui.notify(f'選択: {row["名称"]}')
        # ここに行タップ時の処理を書く

    def open_map(row):
        ui.navigate.to(f'/map/{row["緯度"]}/{row["経度"]}')

    table = ui.table(
        columns=columns,
        rows=rows,
        row_key="コード",
    ).props("flat bordered")

    table.on("row-click", row_clicked)

    with table.add_slot("body-cell-map", r"""
    <q-td :props="props">
        <q-btn
            flat
            round
            dense
            icon="map"
            color="primary"
            @click.stop="$parent.$emit('map-click', props.row)"
        />
    </q-td>
    """):
        pass

    table.on("map-click", lambda e: open_map(e.args))
    floating_nav("table")


# lambda e: ui.navigate.to(f"/map/{e.args[1]["緯度"]}/{e.args[1]["経度"]}")

def map_page(lat: float, lon: float):
    ui.leaflet(center=(lat, lon), zoom=10)
    ui.link("Back to table", "/")
    floating_nav("table")


def settings_page():
    floating_nav("settings")



def floating_nav(current: str):
    tabs = [
        ("table_chart", "一覧", "/", "table"),
        ("settings", "設定", "/settings", "settings"),
    ]

    with ui.element("div").style("""
        position: fixed;
        bottom: 24px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        gap: 8px;
        padding: 8px;

        background: rgba(255,255,255,.18);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);

        border-radius: 999px;
        border: 1px solid rgba(255,255,255,.25);
        box-shadow: 0 8px 32px rgba(0,0,0,.25);

        z-index:9999;
    """):

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


# PWA化
app.add_static_files("/static", "static")

ui.add_head_html("""
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
)
