def css_table_menu():
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