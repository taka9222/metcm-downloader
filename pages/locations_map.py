from nicegui import ui
from pages.settings_page import get_setting
from config.map_tiles import MAP_TILES


def set_map_type(map_element, map_type: str):
    tile = MAP_TILES[map_type]

    map_element.clear_layers()
    map_element.tile_layer(
        url_template=tile["url"],
        options=tile["options"],
    )


def map_page(lat: float, lon: float):
    with ui.element("div").classes("map-page"):

        map_element = ui.leaflet(center=(lat, lon), zoom=get_setting("map_zoom")).classes("map-view")
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
    # これはcallback用の関数なのでmep_elementが定義されていなくてもOK
    set_map_type(map_element, get_setting("map_type"))