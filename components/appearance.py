from nicegui import ui

from config.colors import UI_COLORS

# =========================================================
# Appearance
# =========================================================

BODY_CLASSES = [
    "theme-default",
    "theme-olive",
    "theme-olive-dark",
]


def change_appearance(value: str):
    apply_appearance(value)
    ui.navigate.reload()


def apply_appearance(value: str):
    # bodyクラスをリセット
    ui.colors(**UI_COLORS[value])
    dark = ui.dark_mode()
    ui.query("body").classes(remove=" ".join(BODY_CLASSES))

    match value:
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