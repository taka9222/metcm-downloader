from nicegui import app, ui

from components.page_header import page_header
from components.navbar import floating_nav
from config.settings import SETTINGS
from utils.build_info import get_build_number


def settings_page():
    with ui.column().classes("page-content settings-page"):
        page_header("SETTINGS", "設定")
        ui.label("*は現在未実装")
        settings_section("GENERAL", "一般", ["appearance", "unit"])
        settings_section("WEATHER", "気象情報", ["weather_source", "maximum_zone"])
        settings_section("MAP", "地図", ["map_type", "map_zoom"])
        settings_section("LOCATIONS", "演習場", ["domestic_locations", "foreign_locations", "favorites"])
        settings_section("APP", "アプリ", ["notifications", "help", "version"])

        # Floating Navigation と重ならないように
        ui.element("div").style("height: calc(110px + env(safe-area-inset-bottom));")

        ui.separator()

        with ui.row().classes("w-full"):
            ui.label(f"Build {get_build_number()}").classes("text-xs text-gray-400")

    floating_nav("settings")

# =========================================================
# Settings Section
# =========================================================

def settings_section(eyebrow: str, title: str, keys: list[str]):
    with ui.column().classes("settings-section"):
        with ui.row().classes("settings-section-header"):
            ui.label(eyebrow).classes("settings-section-eyebrow")
            ui.label(title).classes("settings-section-title")

        with ui.element("div").classes("settings-card"):
            settings_table(keys)


def settings_table(keys):
    rows = [
        {
            "key": key,
            "icon": SETTINGS[key]["icon"],
            "title": SETTINGS[key]["title"],
            "value": get_setting_label(key),
            "right_arrow": SETTINGS[key].get("right_arrow", True),
        }
        for key in keys
    ]

    columns = [
        {"name": "title", "label": "", "field": "title", "align": "left"},
        {"name": "value", "label": "", "field": "value", "align": "right"},
    ]

    table = ui.table(columns=columns, rows=rows, row_key="key").classes("settings-table")

    # Row
    table.add_slot(
        "body",
        r"""
        <q-tr :props="props" class="settings-table-row"
              @click="$parent.$emit('row-click', props.row)">

            <!-- Left -->
            <q-td key="title" :props="props" class="settings-table-title-cell">
                <div class="settings-table-title">
                    <q-icon :name="props.row.icon" class="settings-table-icon" />
                    <span>{{ props.row.title }}</span>
                </div>
            </q-td>

            <!-- Right -->
            <q-td key="value" :props="props" class="settings-table-value-cell">
                <div class="settings-table-value">
                    <span>{{ props.row.value }}</span>
                    <q-icon v-if="props.row.right_arrow" name="chevron_right"
                            class="settings-table-arrow" />
                </div>
            </q-td>

        </q-tr>
        """,
    )

    # Update table
    def refresh():
        for row in rows:
            row["value"] = get_setting_label(row["key"])

        table.update_rows(rows)

    # Row click
    def handle_row_click(e):
        key = e.args["key"]
        if e.args["value"] == "" and e.args["right_arrow"]:
            apply_setting(key, None)
        else:
            open_setting_dialog(key, on_changed=refresh)

    table.on("row-click", handle_row_click)

    return table


def get_setting(key: str):
    setting = SETTINGS[key]

    # 固定表示項目
    if not setting["options"]:
        return setting.get("value", "")

    if key not in app.storage.user:
        app.storage.user[key] = setting["default"]

    return app.storage.user[key]


def set_setting(key: str, value: str):
    app.storage.user[key] = value


def get_setting_label(key: str):
    setting = SETTINGS[key]
    value = get_setting(key)

    # 固定表示項目
    if not setting["options"]:
        return value

    return setting["options"].get(value, value)

# =========================================================
# Storage
# =========================================================

def apply_setting(key: str, value: str):
    is_selectable = len(SETTINGS[key].get("options", {})) > 0
    handler = SETTINGS[key].get("on_change")

    if handler is None:
        return 

    if isinstance(handler, str):
        handler = globals().get(handler)
    if is_selectable:
        handler(value)
    else:
        handler()

# =========================================================
# Setting Dialog
# =========================================================

def open_setting_dialog(key: str, on_changed=None):
    setting = SETTINGS[key]

    # 選択肢がない項目はダイアログを開かない
    if not setting["options"]:
        return

    current = get_setting(key)

    with ui.dialog() as dialog:
        with ui.card().classes("setting-dialog"):
            # Header
            with ui.row().classes("setting-dialog-header"):
                ui.label(setting["title"]).classes("setting-dialog-title")
                ui.button(icon="close", on_click=dialog.close).props("flat round dense")

            # Options
            with ui.column().classes("setting-options"):
                for value, label in setting["options"].items():

                    def select(value=value):
                        set_setting(key, value)
                        apply_setting(key, value)

                        if on_changed:
                            on_changed()

                        dialog.close()

                    with ui.element("div").classes("setting-option").on("click", select):
                        ui.label(label).classes("setting-option-label")

                        check = ui.icon("check").classes("setting-option-check")
                        check.set_visibility(value == current)

    dialog.open()