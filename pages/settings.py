from nicegui import app, ui

from config.settings import SETTINGS



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