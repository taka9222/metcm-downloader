from nicegui import ui

from components.page_header import page_header
from components.dialog import dialog_latest_weather
from components.navbar import floating_nav


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
            ui.button("最新データを取得", icon="refresh", 
                      on_click=lambda: dialog_latest_weather(35.0, 135.0),).props(
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