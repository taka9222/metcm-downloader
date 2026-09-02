from nicegui import ui

from config.announcements import ANNOUNCEMENTS

def announcement_card():

    if not ANNOUNCEMENTS:
        return

    with ui.card().classes("w-full announcement-card"):

        with ui.row().classes("announcement-header"):
            with ui.element("div").classes("announcement-icon"):
                ui.icon("campaign")

            with ui.column().classes("announcement-heading"):
                ui.label("ANNOUNCEMENT").classes("announcement-eyebrow")
                ui.label("お知らせ").classes("announcement-title")

        with ui.column().classes("announcement-content w-full") as content:

            items = []

            for i, (date, text) in enumerate(ANNOUNCEMENTS):
                with ui.row().classes("announcement-item") as item:
                    ui.label(date).classes("announcement-date")
                    ui.label(text).classes("announcement-text")

                if i >= 3:
                    item.set_visibility(False)

                items.append(item)

        # 4件以上ある場合のみボタンを表示
        if len(ANNOUNCEMENTS) > 3:
            expanded = False

            with ui.row().classes("announcement-toggle"):
                button = ui.button(
                    "すべて表示",
                    icon="expand_more",
                ).props("flat")

                def toggle():
                    nonlocal expanded
                    expanded = not expanded

                    for i, item in enumerate(items):
                        item.set_visibility(expanded or i < 3)

                    button.text = "折り畳む" if expanded else "すべて表示"
                    button.props(
                        "icon=expand_less"
                        if expanded
                        else "icon=expand_more"
                    )

                button.on("click", toggle)