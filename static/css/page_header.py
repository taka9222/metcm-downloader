def css_page_header():
    return """

.page-header {
    --header-title: #1d1d1f;
    --header-secondary: rgba(60, 60, 67, 0.58);
    --header-line: rgba(60, 60, 67, 0.18);

    width: 100%;
    padding: 6px 4px 22px 4px;
    gap: 3px;
}

.body--dark .page-header {
    --header-title: #f5f5f7;
    --header-secondary: rgba(235, 235, 245, 0.58);
    --header-line: rgba(235, 235, 245, 0.18);
}

.page-header-kicker {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--header-secondary);
}

.page-header-title-group {
    width: fit-content;
    gap: 0;
}

.page-header-title {
    font-size: clamp(28px, 7vw, 36px);
    line-height: 1.1;
    font-weight: 750;
    letter-spacing: -0.04em;
    color: var(--header-title);
}

.page-header-line {
    width: 100%;
    height: 1px;
    margin-top: 10px;
    border-radius: 999px;
    background: var(--header-line);
}
"""