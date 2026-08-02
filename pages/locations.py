from nicegui import ui

from components.page_header import page_header
from components.dialog import dialog_latest_weather
from components.navbar import floating_nav


def locations_page():
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


def create_range_table(rows, overseas=False):
    columns = [
        {"name": "loc", "label": "場所", "field": "loc", "align": "left"},
        {"name": "menu", "label": "", "field": "menu", "style": "width: 48px", "align": "center"},
    ]
    table = ui.table(columns=columns, rows=rows, row_key="code").props(
        "flat bordered hide-header"
    ).classes("w-full glass-table")

    async def row_clicked(e):
        row = e.args[1]
        await dialog_latest_weather(row["lat"], row["lon"])

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