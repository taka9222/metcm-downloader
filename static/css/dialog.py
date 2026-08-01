def css_dialog():
    return """

    /* =========================================================
   Weather Dialog
   ========================================================= */

.weather-dialog {
    width: 560px;
    max-width: calc(100vw - 32px);
    min-height: 360px;
    padding: 32px 36px 28px;
    border: 1px solid rgba(30, 45, 60, 0.16);
    border-radius: 22px;
    background: rgba(255, 255, 255, 0.97);
    box-shadow:
        0 20px 60px rgba(20, 30, 40, 0.16),
        0 4px 16px rgba(20, 30, 40, 0.06);
}

/* ---------------------------------------------------------
   Header
   --------------------------------------------------------- */

.dialog-eyebrow {
    margin-bottom: 4px;
    color: #8b969f;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.18em;
}

.dialog-title {
    color: #182635;
    font-size: 28px;
    font-weight: 800;
    line-height: 1.3;
    letter-spacing: -0.03em;
}

.dialog-separator {
    margin: 12px 0 28px;
    background: rgba(30, 45, 60, 0.14);
}

/* ---------------------------------------------------------
   Information
   --------------------------------------------------------- */

.dialog-info {
    gap: 8px;
}

.dialog-section-label {
    margin-bottom: 2px;
    color: #8b969f;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.18em;
}

.dialog-time {
    color: #172738;
    font-size: 20px;
    font-weight: 700;
    line-height: 1.4;
}

.dialog-age {
    color: #008c9a;
    font-size: 14px;
    font-weight: 700;
}

.dialog-file-row {
    width: 100%;
    margin-top: 18px;
    padding: 13px 16px;
    gap: 10px;
    align-items: center;
    border: 1px solid rgba(30, 45, 60, 0.10);
    border-radius: 10px;
    background: rgba(245, 247, 249, 0.8);
}

.dialog-file-icon {
    color: #8c99a3;
    font-size: 19px;
}

.dialog-filename {
    overflow: hidden;
    color: #687681;
    font-family: monospace;
    font-size: 12px;
    text-overflow: ellipsis;
    white-space: nowrap;
}

/* ---------------------------------------------------------
   Actions
   --------------------------------------------------------- */

.dialog-actions {
    width: 100%;
    justify-content: flex-end;
    align-items: center;
    gap: 6px;
    flex-wrap: wrap;
}

.dialog-button,
.dialog-cancel-button {
    min-height: 42px;
    border-radius: 10px;
    color: #43515d;
    font-weight: 600;
}

.dialog-primary-button {
    min-height: 42px;
    padding: 0 18px;
    border-radius: 10px;
    background: #147bd1 !important;
    color: white !important;
    font-weight: 700;
}

.dialog-cancel-button {
    color: #8a949c;
}

"""