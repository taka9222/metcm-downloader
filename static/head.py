from nicegui import ui   

from static.css.page_header import css_page_header
from static.css.hero_card import css_hero_card

from static.js.service_worker import js_service_worker
from static.js.floating_nav import js_floating_nav

# ============================================================
# CSSを一括登録
# ============================================================

def add_css():
    ui.add_head_html(
        f"""
        <style>
        {css_common()}
        {css_page_header()}
        {css_hero_card()}
        {css_glass_menu()}
        {css_loading_panel()}
        {css_floating_nav()}
        {css_glass_table()}
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
    max-width: 1400px;
    margin: 0 auto;

    padding: clamp(20px, 3vw, 48px)
             clamp(16px, 4vw, 64px)
             calc(
                 clamp(32px, 4vw, 56px)
                 + 100px
                 + env(safe-area-inset-bottom)
             );

    box-sizing: border-box;
}
    """

# ============================================================
# Glass Menu
# ============================================================

def css_glass_menu():
    return """
    .glass-menu {
        backdrop-filter: blur(24px) saturate(180%);
        -webkit-backdrop-filter: blur(24px) saturate(180%);
        background: rgba(255,255,255,.60);
        border: 1px solid rgba(255,255,255,.35);
        border-radius: 18px;
        box-shadow:
            0 10px 40px rgba(0,0,0,.18),
            inset 0 1px rgba(255,255,255,.35);
        overflow: hidden;
    }

    .body--dark .glass-menu,
    .theme-olive-dark .glass-menu {
        background: rgba(40,40,40,.55);
        border: 1px solid rgba(255,255,255,.12);
        box-shadow:
            0 10px 40px rgba(0,0,0,.35),
            inset 0 1px rgba(255,255,255,.08);
    }

    .glass-menu .q-item {
        min-height: 44px;
        border-radius: 12px;
        margin: 4px;
        transition: background .15s;
    }

    .glass-menu .q-item__section--avatar {
        min-width: 36px;
    }

    .glass-menu .q-item:hover {
        background: rgba(255,255,255,.18);
    }

    .glass-menu .q-item:active {
        background: rgba(255,255,255,.28);
    }

    .q-menu__content {
        z-index: 10000 !important;
        border-radius: 20px;
        overflow: hidden;
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
# Floating Navigation Bar
# ============================================================

def css_floating_nav():
    return """
    .floating-nav {
        --nav-index: 0;
        --nav-count: 3;
        position: fixed;
        left: 50%;
        bottom: calc(14px + env(safe-area-inset-bottom));
        width: min(360px, calc(100vw - 32px));
        height: 68px;
        transform: translateX(-50%);
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        padding: 5px;
        border-radius: 999px;
        backdrop-filter: blur(28px) saturate(180%);
        -webkit-backdrop-filter: blur(28px) saturate(180%);
        background: var(--color-nav-bg-light);
        border: 1px solid rgba(25, 25, 25, .16);
        box-shadow:
            0 8px 30px rgba(0, 0, 0, .12),
            inset 0 1px 0 rgba(255, 255, 255, .55);
        z-index: 9999;
        touch-action: none;
        user-select: none;
        -webkit-user-select: none;
        -webkit-tap-highlight-color: transparent;
        isolation: isolate;
    }


    /* 選択カーソル */
    .floating-nav-cursor {
        position: absolute;
        top: 5px;
        left: 5px;
        width: calc((100% - 10px) / var(--nav-count));
        height: calc(100% - 10px);
        border-radius: 999px;
        background: rgba(255, 255, 255, .42);
        border: 1px solid rgba(25, 25, 25, .16);
        box-shadow:
            inset 0 1px 0 rgba(255, 255, 255, .55),
            0 2px 8px rgba(0, 0, 0, .08);
        transform: translateX(calc(var(--nav-index) * 100%));
        transition: transform .28s cubic-bezier(.2, .8, .2, 1);
        pointer-events: none;
        z-index: 0;
    }


    /* Dark Mode */
    .body--dark .floating-nav {
        background: var(--color-nav-bg-dark);
        border: 1px solid rgba(255, 255, 255, .16);
    }
    
    .body--dark .floating-nav-cursor {
        background: rgba(255, 255, 255, .12);
        border: 1px solid rgba(255, 255, 255, .16);
        box-shadow:
            inset 0 1px 0 rgba(255, 255, 255, .18),
            0 2px 8px rgba(0, 0, 0, .18);
    }


    /* 各項目 */
    .floating-nav-item {
        position: relative;
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 3px;
        border-radius: 19px;
        cursor: pointer;
        z-index: 1;
        transition: transform .15s ease;
        -webkit-tap-highlight-color: transparent;
    }

    /* アイコン */
    .floating-nav-icon {
        font-size: 21px;
        line-height: 1;
        opacity: .75;
        transition:
            transform .2s ease,
            opacity .2s ease;
    }

    /* 文字 */
    .floating-nav-label {
        font-size: 10px;
        line-height: 1.1;
        font-weight: 500;
        white-space: nowrap;
        opacity: .70;
        transition:
            opacity .2s ease,
            font-weight .2s ease;
    }

    /* アクティブ */
    .floating-nav-item.is-active .floating-nav-icon {
        opacity: 1;
        transform: scale(1.04);
    }

    .floating-nav-item.is-active .floating-nav-label {
        opacity: 1;
        font-weight: 600;
    }

    /* 押したとき */
    .floating-nav-item:active {
        transform: scale(.94);
    }
    """

# ============================================================
# Glass Table
# ============================================================

def css_glass_table():
    return """
    .glass-table {
        border-radius: 18px;
        overflow: hidden;
        background: rgba(235, 237, 240, .72) !important;
        border: 1px solid rgba(110, 115, 122, .28) !important;
        backdrop-filter: blur(20px) saturate(120%);
        -webkit-backdrop-filter: blur(20px) saturate(120%);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.10);
    }


    /* テーブル内部は透明にして、外側のガラスを見せる */
    .glass-table .q-table__container,
    .glass-table .q-table__middle {
        background: transparent !important;
    }


    /* Header */
    .glass-table thead tr {
        background: rgba(220, 223, 227, .82);
    }

    .glass-table thead th {
        background: transparent !important;
        font-weight: 600;
        border-bottom: 1px solid rgba(100, 105, 112, .22) !important;
    }

    /* Body */
    .glass-table tbody tr {
        background: rgba(255, 255, 255, .38);
        transition: background .15s ease;
    }

    .glass-table tbody td {
        border-color:
            rgba(100, 105, 112, .14) !important;
    }

    /* Hover */
    .glass-table tbody tr:hover {
        background: rgba(220, 223, 227, .55);
    }

    /* Dark Mode */
    .body--dark .glass-table {
        background: rgba(38, 39, 41, .55) !important;
        border-color: rgba(255, 255, 255, .15) !important;
    }

    .body--dark .glass-table thead tr {
        background: rgba(255, 255, 255, .09);
    }

    .body--dark .glass-table tbody tr {
        background: rgba(255, 255, 255, .025);
    }

    .body--dark .glass-table tbody tr:hover {
        background: rgba(255, 255, 255, .08);
    }

    .body--dark .glass-table tbody td {
        border-color: rgba(255, 255, 255, .08) !important;
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
