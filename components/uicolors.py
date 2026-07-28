from nicegui import ui

BODY_CLASSES = [
    "theme-default",
    "theme-olive",
    "theme-olive-dark",
    "theme-jsdf",
]

dark = ui.dark_mode()

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
