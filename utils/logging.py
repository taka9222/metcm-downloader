# utils/logging.py

import logging
from nicegui import ui


logger = logging.getLogger("metcm-downloader")


def debug_log(message: str) -> None:
    logger.debug(message)
    ui.run_javascript(f"console.log({message!r})")