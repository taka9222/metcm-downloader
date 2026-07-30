from nicegui import ui   

from static.css.page_header import css_page_header
from static.css.hero_card import css_hero_card
from static.css.table import css_table
from static.css.table_menu import css_table_menu
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
        {css_hero_card()}
        {css_table()}
        {css_table_menu()}
        {css_loading_panel()}
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

    padding: clamp(16px, 3vw, 40px)
             clamp(12px, 3vw, 39px)
             calc(
                 clamp(24px, 4vw, 48px)
                 + 100px
                 + env(safe-area-inset-bottom)
             );

    box-sizing: border-box;
}
    """


# ============================================================
# Glass Loading Panel
# ============================================================

def css_loading_panel():
    return """
    .loading-card {
        width: 300px;
        padding: 28px 26px;
        background: rgba(238, 239, 241, 0.78);
        backdrop-filter: blur(40px) saturate(150%);
        -webkit-backdrop-filter: blur(40px) saturate(150%);
        border-radius: 28px;
        border: 1px solid rgba(70, 72, 76, 0.18);
        box-shadow:
            0 20px 60px rgba(0,0,0,0.12),
            0 4px 16px rgba(0,0,0,0.05),
            inset 0 1px 0 rgba(255,255,255,0.72);
        overflow: hidden;
        isolation: isolate;
    }

    .loading-spinner {
        margin-bottom: 14px;
    }

    .loading-message {
        width: 100%;
        margin-top: 0;
        font-size: 13px;
        line-height: 1.5;
        color: rgba(40,42,45,0.52);
        text-align: center;
        letter-spacing: -0.005em;
    }

    /* Dark Mode */
    .body--dark .loading-card {
        background: rgba(30,31,34,0.76);
        border: 1px solid rgba(255,255,255,0.14);
        box-shadow:
            0 20px 60px rgba(0,0,0,0.32),
            0 4px 16px rgba(0,0,0,0.18),
            inset 0 1px 0 rgba(255,255,255,0.10);
    }

    .body--dark .loading-message {
        color: rgba(255,255,255,0.52);
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
