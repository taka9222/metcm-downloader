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


/* =========================================================
   Dark mode
   ========================================================= */

.body--dark .weather-dialog {
    border-color: rgba(255, 255, 255, 0.10);

    background: rgba(30, 34, 39, 0.97);

    box-shadow:
        0 20px 60px rgba(0, 0, 0, 0.42),
        0 4px 16px rgba(0, 0, 0, 0.24);
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

.body--dark .dialog-eyebrow {
    color: #8f9aa3;
}


.dialog-title {
    color: #182635;

    font-size: 28px;
    font-weight: 800;

    line-height: 1.3;
    letter-spacing: -0.03em;
}

.body--dark .dialog-title {
    color: #edf1f4;
}


.dialog-separator {
    margin: 12px 0 28px;

    background: rgba(30, 45, 60, 0.14);
}

.body--dark .dialog-separator {
    background: rgba(255, 255, 255, 0.12);
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

.body--dark .dialog-section-label {
    color: #929da5;
}


.dialog-time {
    color: #172738;

    font-size: 20px;
    font-weight: 700;

    line-height: 1.4;
}

.body--dark .dialog-time {
    color: #e7edf1;
}


.dialog-age {
    color: #008c9a;

    font-size: 14px;
    font-weight: 700;
}

.body--dark .dialog-age {
    color: #49b9c3;
}


/* ---------------------------------------------------------
   File information
   --------------------------------------------------------- */

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

.body--dark .dialog-file-row {
    border-color: rgba(255, 255, 255, 0.09);

    background: rgba(255, 255, 255, 0.045);
}


.dialog-file-icon {
    color: #8c99a3;

    font-size: 19px;
}

.body--dark .dialog-file-icon {
    color: #9ba6ae;
}


.dialog-filename {
    overflow: hidden;

    color: #687681;

    font-family: monospace;
    font-size: 12px;

    text-overflow: ellipsis;
    white-space: nowrap;
}

.body--dark .dialog-filename {
    color: #aeb8bf;
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

.body--dark .dialog-button,
.body--dark .dialog-cancel-button {
    color: #c2cbd1;
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

.body--dark .dialog-cancel-button {
    color: #9ba5ad;
}


/* =========================================================
   Mobile
   ========================================================= */

@media (max-width: 600px) {

    .weather-dialog {
        width: calc(100vw - 24px);
        max-width: none;

        padding: 26px 22px 22px;

        border-radius: 18px;
    }


    .dialog-title {
        font-size: 24px;
    }


    .dialog-separator {
        margin: 10px 0 24px;
    }


    .dialog-actions {
        justify-content: stretch;
    }


    .dialog-primary-button,
    .dialog-cancel-button,
    .dialog-button {
        min-height: 40px;
    }
}

"""
