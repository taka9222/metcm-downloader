from nicegui import ui

def floating_nav(current: str):
    tabs = [
        ("table_chart", "一覧", "/", "table"),
        ("settings", "設定", "/settings", "settings"),
    ]

    with ui.element("div").classes("floating-nav"):

        for icon, label, path, name in tabs:

            active = (current == name)

            ui.button(
                label if active else "",
                icon=icon,
                on_click=lambda p=path: ui.navigate.to(p),
            ).props(
                "unelevated no-caps rounded" if active else "flat round"
            ).style(f"""
                width: {'120px' if active else '48px'};
                height:48px;
                border-radius:999px;

                transition:

                    all .25s cubic-bezier(.2,.8,.2,1);

                {'background:rgba(255,255,255,.35);' if active else ''}
            """)