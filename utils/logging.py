# utils/logging.py

import logging

logger = logging.getLogger(__name__)


def debug_log(message: str) -> None:
    print(message)
    logger.debug(message)