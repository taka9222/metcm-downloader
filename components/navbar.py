from nicegui import ui


def floating_nav(current: str):
    tabs = [
        ("home", "ホーム", "/", "home"),
        ("map", "演習場一覧", "/table", "table"),
        ("settings", "設定", "/settings", "settings"),
    ]

    current_index = next(
        (
            i
            for i, (_, _, _, name) in enumerate(tabs)
            if name == current
        ),
        0,
    )

    with ui.element("div").classes("floating-nav") as nav:

        # 選択カーソル
        ui.element("div").classes("floating-nav-cursor")

        # ナビゲーション項目
        for index, (icon, label, path, name) in enumerate(tabs):

            item = (
                ui.element("div").classes("floating-nav-item").props(f'data-index="{index}"')
            )

            if index == current_index:
                item.classes(add="is-active")

            with item:
                ui.icon(icon).classes("floating-nav-icon")
                ui.label(label).classes("floating-nav-label")

            # 通常クリック
            item.on(
                "click",
                lambda _, p=path: ui.navigate.to(p),
            )

    # 初期状態
    def update_nav_position():
        ui.run_javascript(f"""
            const nav = document.querySelector('.floating-nav');

            if (!nav) return;

            nav.style.setProperty('--nav-index', '{current_index}');
            nav.style.setProperty('--nav-count', '{len(tabs)}');
        """)

    ui.timer(0, update_nav_position, once=True)