# utils/build_info.py

from __future__ import annotations

import os


def get_build_number() -> str:
    """現在のビルドを識別する番号を返す."""
    commit = os.getenv("RENDER_GIT_COMMIT")

    if commit:
        return commit[:7]

    return "dev"