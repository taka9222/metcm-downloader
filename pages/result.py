from __future__ import annotations

from nicegui import app, ui

from components.navbar import floating_nav
from components.page_header import page_header


FORMAT_OPTIONS = {
    "metcm_gsdf": "陸上自衛隊弾道計算気象報",
    "metcm_stanag": "STANAG 4082 弾道計算気象報",
    "full_content": "一覧表示",
}


def result_page():
    """解析結果を表示するページ。"""

    result = app.storage.tab.get("atmospheric_result")

    with ui.column().classes("page-content result-page"):

        # -------------------------------------------------
        # Back
        # -------------------------------------------------

        ui.button(
            "選択画面に戻る", icon="arrow_back", on_click=ui.navigate.back,
        ).props("flat no-caps").classes("result-back-button")

        # -------------------------------------------------
        # Header
        # -------------------------------------------------

        page_header("RESULT", "気象解析結果")

        if not result:
            ui.label(
                "表示できる解析結果がありません。"
            ).classes("result-empty-message")

            ui.button(
                "選択画面に戻る", on_click=lambda: ui.navigate.back,
            ).props("unelevated no-caps")

            return

        layers = result["layers"]
        source = result["source"]
        lat = result["lat"]
        lon = result["lon"]

        # -------------------------------------------------
        # Metadata
        # -------------------------------------------------

        with ui.card().classes("result-info-card"):

            ui.label("ATMOSPHERIC PROFILE").classes("dialog-eyebrow")
            ui.label("大気層気象データ").classes("dialog-title")

            ui.separator().classes("dialog-separator")

            with ui.row().classes("atmosphere-meta"):

                ui.label(f"LAT {lat:.4f}").classes("atmosphere-location")
                ui.label(f"LON {lon:.4f}").classes("atmosphere-location")

            ui.label(source["time"].strftime("%Y年 %m月 %d日 %H00 UTC")).classes("dialog-age")

        # -------------------------------------------------
        # Format selector
        # -------------------------------------------------

        with ui.row().classes("result-format-row"):

            ui.label("表示形式").classes("result-format-label")

            format_select = ui.select(
                FORMAT_OPTIONS, value="metcm_gsdf",
            ).props("outlined dense").classes("result-format-select")

        # -------------------------------------------------
        # Table
        # -------------------------------------------------

        table_container = ui.column().classes("w-full result-table-container")

        def update_table():
            table_container.clear()

            with table_container:
                if format_select.value == "metcm_gsdf":
                    _show_gsdf_table(layers)

                elif format_select.value == "metcm_stanag":
                    _show_stanag_table(layers)

                elif format_select.value == "full_content":
                    _show_full_table(layers)

        format_select.on_value_change(
            lambda _: update_table()
        )

        update_table()

        # -------------------------------------------------
        # Footer
        # -------------------------------------------------

        ui.element("div").style("height: calc(110px + env(safe-area-inset-bottom));")


def _show_gsdf_table(layers: list[dict]):
    """自衛隊形式の大気層表を表示する。"""

    columns = [
        {
            "name": "zone",
            "label": "ZONE",
            "field": "zone",
            "align": "center",
        },
        {
            "name": "wind_direction",
            "label": "風向\n[10 mils]",
            "field": "wind_direction",
            "align": "center",
        },
        {
            "name": "wind_speed",
            "label": "風速\n[0.1 m/sec]",
            "field": "wind_speed",
            "align": "center",
        },
        {
            "name": "virtual_temperature",
            "label": "弾道気温\n[0.1 K]",
            "field": "virtual_temperature",
            "align": "center",
        },
        {
            "name": "density",
            "label": "空気密度\n[g/m3]",
            "field": "density",
            "align": "center",
        },
    ]

    rows = []

    for layer in layers:
        rows.append(
            {
                "zone": f'{layer["zone"]:02d}',
                "wind_direction": f'{round(layer["wind_direction"] / 10):03d}',
                "wind_speed": f'{round(layer["wind_speed"] * 10):03d}',
                "virtual_temperature": f'{round(layer["virtual_temperature"] * 10):04d}',
                "density": f'{round(layer['density']):04d}',
            }
        )

    ui.table(columns=columns, rows=rows, row_key="zone").classes("atmosphere-table")


def _show_stanag_table(layers: list[dict]):
    """STANAG形式の大気層表を表示する。"""

    columns = [
        {
            "name": "zone",
            "label": "ZONE",
            "field": "zone",
            "align": "center",
        },
        {
            "name": "wind_direction",
            "label": "風向\n[10 mils]",
            "field": "wind_direction",
            "align": "center",
        },
        {
            "name": "wind_speed",
            "label": "風速\n[kt]",
            "field": "wind_speed",
            "align": "center",
        },
        {
            "name": "virtual_temperature",
            "label": "気温\n[0.1 K]",
            "field": "virtual_temperature",
            "align": "center",
        },
        {
            "name": "pressure",
            "label": "気圧\n[hPa]",
            "field": "pressure",
            "align": "center",
        },
    ]

    rows = []

    for layer in layers:
        wind_speed_kt = layer["wind_speed"] * 1.943844

        rows.append(
            {
                "zone": f'{layer["zone"]:02d}',
                "wind_direction": f'{round(layer["wind_direction"] / 10):03d}',
                "wind_speed": f'{round(wind_speed_kt):03d}',
                "virtual_temperature": f'{round(layer["virtual_temperature"] * 10):04d}',
                "pressure": f'{round(layer["pressure"]):04d}',
            }
        )

    ui.table(columns=columns, rows=rows, row_key="zone").classes("atmosphere-table")


def _show_full_table(layers: list[dict]):
    """完全形式の大気層表を表示する。"""

    columns = [
        {
            "name": "zone",
            "label": "ZONE",
            "field": "zone",
            "align": "center",
        },
        {
            "name": "bottom",
            "label": "BOTTOM\n[m]",
            "field": "bottom",
            "align": "center",
        },
        {
            "name": "height",
            "label": "HEIGHT\n[m]",
            "field": "height",
            "align": "center",
        },
        {
            "name": "top",
            "label": "TOP\n[m]",
            "field": "top",
            "align": "center",
        },
        {
            "name": "density",
            "label": "空気密度\n[g/m3]",
            "field": "density",
            "align": "center",
        },
        {
            "name": "temperature",
            "label": "気温\n[K]",
            "field": "temperature",
            "align": "center",
        },
        {
            "name": "virtual_temperature",
            "label": "弾道気温\n[K]",
            "field": "virtual_temperature",
            "align": "center",
        },
        {
            "name": "pressure",
            "label": "気圧\n[hPa]",
            "field": "pressure",
            "align": "center",
        },
        {
            "name": "wind_speed",
            "label": "風速\n[m/sec]",
            "field": "wind_speed",
            "align": "center",
        },
        {
            "name": "wind_direction",
            "label": "風向\n[mils]",
            "field": "wind_direction",
            "align": "center",
        },
        {
            "name": "relative_humidity",
            "label": "湿度\n[%]",
            "field": "relative_humidity",
            "align": "center",
        },
    ]

    rows = [
        {
            "zone": f'{layer["zone"]:02d}',
            "bottom": f'{layer["bottom"]:.0f}',
            "height": f'{layer["height"]:.0f}',
            "top": f'{layer["top"]:.0f}',
            "density": f'{layer["density"]:.0f}',
            "temperature": f'{layer["temperature"]:.1f}',
            "virtual_temperature": f'{layer["virtual_temperature"]:.1f}',
            "pressure": f'{layer["pressure"]:.0f}',
            "wind_speed": f'{layer["wind_speed"]:.1f}',
            "wind_direction": f'{layer["wind_direction"]:.0f}',
            "relative_humidity": f'{layer["relative_humidity"]:.3f}',
        }
        for layer in layers
    ]

    ui.table(columns=columns, rows=rows, row_key="zone").classes("atmosphere-table")