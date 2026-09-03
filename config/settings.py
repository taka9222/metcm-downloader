from components.appearance import change_appearance
from pages.help_page import open_help_page


SETTINGS = {
    "appearance": {
        "icon": "dark_mode",
        "title": "外観",
        "options": {
            "system": "システム設定に従う",
            "light": "ライト",
            "dark": "ダーク",
            "olive":"オリーブドラブ",
            "olive_dark": "オリーブドラブ (濃)"
        },
        "default": "system",
        "on_change": change_appearance,
    },
    "unit": {
        "icon": "straighten",
        "title": "単位系*",
        "options": {"metric": "Metric", "imperial": "Imperial"},
        "default": "metric",
    },
    "weather_source": {
        "icon": "cloud",
        "title": "データソース*",
        "options": {"fnl": "FNL"},
        "default": "fnl",
    },
    "maximum_zone": {
        "icon": "cloud",
        "title": "最大気層",
        "options": {"8": "8", "12": "12", "16": "16", "20": "20", "26": "26", "31": "31"},
        "default": "16",
    },
    "map_type": {
        "icon": "map",
        "title": "地図の種類",
        "options": {
            "standard": "デフォルト",
            "satellite": "航空写真",
            "terrain": "地形",
        },
        "default": "standard",
    },
    "map_zoom": {
        "icon": "zoom_in",
        "title": "初期ズーム",
        "options": {"6": "6", "10": "10", "14": "14", "18": "18"},
        "default": "10",
    },
    "domestic_locations": {
        "icon": "flag",
        "title": "国内射場",
        "options": {},
        "default": None,
        "right_arrow": False,
        "value": "9ヶ所",
    },
    "foreign_locations": {
        "icon": "public",
        "title": "国外射場",
        "options": {},
        "default": None,
        "right_arrow": False,
        "value": "2ヶ所",
    },
    "favorites": {
        "icon": "star",
        "title": "お気に入り*",
        "options": {},
        "default": None,
        "right_arrow": True,
        "value": "管理",
    },
    "notifications": {
        "icon": "notifications",
        "title": "通知*",
        "options": {"enabled": "有効", "disabled": "無効"},
        "default": "enabled",
    },
    "help": {
        "icon": "help_outline",
        "title": "操作のヒント",
        "options": {},
        "default": None,
        "right_arrow": True,
        "on_change": open_help_page,
    },
    "version": {
        "icon": "info",
        "title": "バージョン",
        "options": {},
        "default": None,
        "right_arrow": False,
        "value": "0.0.1-alpha",
    },
}