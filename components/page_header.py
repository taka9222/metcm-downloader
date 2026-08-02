from nicegui import ui


def page_header(kicker: str, title: str):
    with ui.column().classes("page-header"):
        ui.label(kicker).classes("page-header-kicker")

        with ui.column().classes("page-header-title-group"):
            ui.label(title).classes("page-header-title")
            ui.element("div").classes("page-header-line")