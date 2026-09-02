def css_announcements():
    return """

/* ========================================
   Announcement Card
   ======================================== */

.announcement-card {
    margin-bottom: 28px;
    padding: 20px 22px;
    border-radius: 20px;

    background: rgba(255, 255, 255, 0.55);

    /* 枠線 */
    border: 1px solid rgba(0, 0, 0, 0.18);

    box-shadow:
        inset 0 1px 0 rgba(255, 255, 255, 0.45),
        0 8px 30px rgba(0, 0, 0, 0.06);

    backdrop-filter: blur(28px) saturate(180%);
    -webkit-backdrop-filter: blur(28px) saturate(180%);

    position: relative;
    overflow: hidden;
}


/* ========================================
   Header
   ======================================== */

.announcement-header {
    align-items: center;
    gap: 12px;
    margin-bottom: 14px;
}

.announcement-icon {
    width: 38px;
    height: 38px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 12px;

    background: rgba(80, 120, 180, 0.12);
}

.announcement-icon .q-icon {
    font-size: 21px;
}

.announcement-heading {
    gap: 0;
}

.announcement-eyebrow {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.12em;
    opacity: 0.55;
}

.announcement-title {
    font-size: 18px;
    font-weight: 650;
    line-height: 1.25;
}


/* ========================================
   Content
   ======================================== */

.announcement-content {
    width: 100%;
    gap: 0;
}

.announcement-item {
    position: relative;
    width: 100% !important;
    align-items: baseline;
    gap: 14px;
    padding: 10px 0;
}

.announcement-item + .announcement-item {
    border-top: 1px solid rgba(0, 0, 0, 0.08);
}

body.body--dark .announcement-item + .announcement-item {
    border-top-color: rgba(255, 255, 255, 0.10);
}

.announcement-date {
    flex: 0 0 auto;

    font-size: 11px;
    font-variant-numeric: tabular-nums;

    opacity: 0.45;
}

.announcement-text {
    font-size: 14px;
    line-height: 1.5;
}


/* ========================================
   Dark Mode
   ======================================== */

body.body--dark .announcement-card {
    background: rgba(255, 255, 255, 0.08);

    /* 枠線 */
    border: 1px solid rgba(255, 255, 255, 0.18);

    box-shadow:
        inset 0 1px 0 rgba(255, 255, 255, 0.10),
        0 8px 30px rgba(0, 0, 0, 0.25);

    backdrop-filter: blur(28px) saturate(180%);
    -webkit-backdrop-filter: blur(28px) saturate(180%);
}

body.body--dark .announcement-icon {
    background: rgba(120, 160, 220, 0.16);
}

body.body--dark .announcement-item + .announcement-item {
    border-top-color: rgba(255, 255, 255, 0.10);
}

body.body--dark .announcement-eyebrow,
body.body--dark .announcement-date {
    opacity: 0.55;
}

/* ========================================
    Toggle Button
   ======================================== */

.announcement-toggle {
    width: 100%;
    justify-content: flex-end;
    margin-top: 4px;
}

.announcement-toggle .q-btn {
    min-height: 32px;
    padding: 0 12px;

    border-radius: 10px;

    font-size: 12px;
    font-weight: 600;

    opacity: 0.65;
}

.announcement-toggle .q-btn:hover {
    opacity: 1;
}

"""