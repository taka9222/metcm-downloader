from nicegui import ui   

from static.css.page_header import css_page_header
from static.css.announcements import css_announcements
from static.css.home_dashboard import css_home_dashboard
from static.css.hero_card import css_hero_card
from static.css.table import css_table
from static.css.table_menu import css_table_menu
from static.css.map import css_map
from static.css.loading_panel import css_loading_panel
from static.css.dialog import css_dialog
from static.css.search_result import css_search_result
from static.css.result import css_result
from static.css.settings import css_settings
from static.css.floating_nav import css_floating_nav

from static.js.service_worker import js_service_worker
from static.js.floating_nav import js_floating_nav

# CSSを一括登録
def add_css():
    ui.add_head_html(
        f"""
        <style>
        {css_common()}
        {css_page_header()}
        {css_announcements()}
        {css_home_dashboard()}
        {css_hero_card()}
        {css_table()}
        {css_table_menu()}
        {css_map()}
        {css_loading_panel()}
        {css_dialog()}
        {css_search_result()}
        {css_result()}
        {css_settings()}
        {css_floating_nav()}
        </style>
        """
    )

def add_script():
    ui.add_head_html(
        f"""
        <script>
        {js_service_worker()}
        {js_floating_nav()}
        </script>
        """
    )

# ============================================================
# 共通
# ============================================================

def css_common():
    return """
    body {
        transition:
            background-color .25s ease,
            color .25s ease,
            background-image .35s ease;
    }

    body.theme-olive {
        background: #596B2D;
    }

    body.theme-olive-dark {
        background: #28311B;
    }

.page-content {
    width: 100%;
    max-width: 1300px;
    margin: 0 auto;

    padding: clamp(8px, 1vw, 20px)
             clamp(6px, 1vw, 20px)
             calc(
                 clamp(12px, 2vw, 24px)
                 + 100px
                 + env(safe-area-inset-bottom)
             );

    box-sizing: border-box;
}

/* =========================================================
   Dialog positioning
   Floating navigation bar を考慮
   ========================================================= */

/*
 * floating-nav:
 *   height: 68px
 *   bottom: 14px + safe-area
 *
 * さらに 16px の余白を確保する。
 *
 * これによりダイアログの中央位置を、
 * 画面全体ではなく「ナビを除いた領域」の中央にする。
 */

.q-dialog__inner {
    padding-top: 0;
    padding-bottom:
        calc(
            68px
            + 14px
            + env(safe-area-inset-bottom)
            + 16px
        );

}

    """


# ============================================================
# その他のHead要素
# ============================================================

def add_manifest():
    """PWA manifestを読み込む"""
    ui.add_head_html("""
        <link rel="manifest" href="/static/manifest.json">
    """)


# ============================================================
# Headを一括登録
# ============================================================

def add_head():
    add_manifest()
    add_css()
    add_script()
