from nicegui import app, ui
import sys
import os
from urllib.request import build_opener
import pygrib

from components.navbar import floating_nav
from components.dialog import dialog_latest_weather
from components.colors import UI_COLORS

 
def home_page():
    ui.label("ホーム").classes("text-h5")
    floating_nav("home")


def table_page():
    ui.label("演習場一覧").classes("text-h5")
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
        # {"name": "code", "label": "コード", "field": "code", "style": "width:60px", "align": "left"},
        {"name": "loc", "label": "場所", "field": "loc", "align": "left"},
        {"name": "latlon", "label": "緯度経度", "field": "latlon", "style": "width:70px", "align": "left"},
        {"name": "menu", "label": "", "field": "menu", "style": "width:48px", "align": "center"},
    ]

    async def row_clicked(e):
        await dialog_latest_weather()

    def open_map(row):
        ui.navigate.to(f'/map/{row["lat"]}/{row["lon"]}')

    table = ui.table(columns=columns, rows=rows, row_key="code").props("flat bordered").classes("w-full")
    table.on("row-click", row_clicked)

    with table.add_slot('body-cell-latlon', r'''
        <q-td :props="props" style="white-space: pre-line;">
        {{ props.value }}
        </q-td>
        '''):
        pass

    with table.add_slot('body-cell-menu', r'''
        <q-td :props="props" auto-width>
        <q-btn flat round dense icon="more_vert" @click.stop="$parent.$emit('menu-click', props.row)">
            <q-menu class="glass-menu" :offset="[0, -24]" >
            <q-list style="min-width:180px">

                <q-item clickable v-close-popup @click="$parent.$emit('map-click', props.row)">
                <q-item-section avatar>
                    <q-icon name="place"/>
                </q-item-section>
                <q-item-section>地図を表示</q-item-section>
                </q-item>

                <q-item clickable v-close-popup @click="$parent.$emit('detail-click', props.row)">
                <q-item-section avatar>
                    <q-icon name="info"/>
                </q-item-section>
                <q-item-section>詳細</q-item-section>
                </q-item>

                <q-item clickable v-close-popup @click="$parent.$emit('favorite-click', props.row)">
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
    table.on("detail-click", lambda e: ui.notify(f'詳細: {e.args["loc"]}', position="top"))
    table.on("favorite-click", lambda e: ui.notify(f'お気に入り: {e.args["loc"]}', position="top"))
    floating_nav("table")


def map_page(lat: float, lon: float):
    ui.leaflet(center=(lat, lon), zoom=10).classes("w-full").style("height: 85vh;")
    floating_nav("table")


def settings_page():
    ui.label("設定").classes("text-h5")

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

ui.add_head_html("""
    <link rel="stylesheet" href="/static/css/style.css">
    <link rel="manifest" href="/static/manifest.json">
    <script>
    if ("serviceWorker" in navigator) {
        navigator.serviceWorker.register("/static/sw.js");
    }
    (() => {
        'use strict';

        const NAV_SELECTOR = '.floating-nav';
        const ITEM_SELECTOR = '.floating-nav-item';

        function initFloatingNav() {
            const nav = document.querySelector(NAV_SELECTOR);

            if (!nav || nav.dataset.initialized === 'true') {
                return;
            }

            nav.dataset.initialized = 'true';

            const items = Array.from(
                nav.querySelectorAll(ITEM_SELECTOR)
            );

            if (!items.length) {
                return;
            }

            const count = items.length;

            let dragging = false;
            let startX = 0;
            let currentIndex = 0;

            /*
            * Pythonから渡された初期値。
            * DOMの内容を信用してURLを作ることはしない。
            */
            const initialIndex = Number(nav.dataset.current);

            if (
                Number.isInteger(initialIndex) &&
                initialIndex >= 0 &&
                initialIndex < count
            ) {
                currentIndex = initialIndex;
            }

            function setIndex(index, animate = true) {
                index = Math.max(
                    0,
                    Math.min(count - 1, index)
                );

                currentIndex = index;

                nav.style.setProperty(
                    '--nav-index',
                    String(index)
                );

                nav.style.setProperty(
                    '--nav-count',
                    String(count)
                );

                if (!animate) {
                    nav.querySelector(
                        '.floating-nav-cursor'
                    )?.style.setProperty(
                        'transition',
                        'none'
                    );
                }

                items.forEach((item, i) => {
                    item.dataset.active =
                        i === index ? 'true' : 'false';
                });
            }

            function updateFromX(clientX) {
                const rect = nav.getBoundingClientRect();

                const x =
                    clientX -
                    rect.left -
                    6;

                const usableWidth =
                    rect.width - 12;

                const raw =
                    x / (usableWidth / count);

                const index = Math.round(raw - 0.5);

                setIndex(index);
            }

            function navigate(index) {
                const item = items[index];

                if (!item) {
                    return;
                }

                /*
                * URLはHTML側から取得しない。
                * data-indexだけをクリックイベントとして
                * NiceGUI側へ渡す。
                */
                item.click();
            }

            nav.addEventListener(
                'pointerdown',
                (event) => {
                    if (event.pointerType === 'mouse' &&
                        event.button !== 0) {
                        return;
                    }

                    dragging = true;

                    startX = event.clientX;

                    nav.setPointerCapture(
                        event.pointerId
                    );

                    nav.classList.add(
                        'is-dragging'
                    );

                    updateFromX(event.clientX);

                    event.preventDefault();
                },
                { passive: false }
            );

            nav.addEventListener(
                'pointermove',
                (event) => {
                    if (!dragging) {
                        return;
                    }

                    updateFromX(event.clientX);

                    event.preventDefault();
                },
                { passive: false }
            );

            nav.addEventListener(
                'pointerup',
                (event) => {
                    if (!dragging) {
                        return;
                    }

                    dragging = false;

                    nav.classList.remove(
                        'is-dragging'
                    );

                    setIndex(currentIndex);

                    navigate(currentIndex);

                    event.preventDefault();
                },
                { passive: false }
            );

            nav.addEventListener(
                'pointercancel',
                () => {
                    dragging = false;

                    nav.classList.remove(
                        'is-dragging'
                    );

                    setIndex(currentIndex);
                }
            );

            /*
            * 通常クリックもサポート。
            */
            items.forEach((item, index) => {
                item.addEventListener(
                    'click',
                    (event) => {
                        if (dragging) {
                            event.preventDefault();
                            return;
                        }

                        setIndex(index);
                    }
                );
            });

            setIndex(currentIndex, false);
        }

        /*
        * NiceGUIのページ遷移やPWA復帰時にも
        * 再初期化できるようにする。
        */
        function observe() {
            initFloatingNav();

            const observer = new MutationObserver(() => {
                initFloatingNav();
            });

            observer.observe(
                document.body,
                {
                    childList: true,
                    subtree: true
                }
            );
        }

        if (
            document.readyState === 'loading'
        ) {
            document.addEventListener(
                'DOMContentLoaded',
                observe,
                { once: true }
            );
        } else {
            observe();
        }
    })();
    </script>
""")

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
