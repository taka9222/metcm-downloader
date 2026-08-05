def css_dialog():
    return """

/* =========================================================
   Weather Dialog
   ========================================================= */

.weather-dialog {
    width: 520px;
    max-width: calc(100vw - 32px);
    min-height: 0;

    padding: 24px 28px 22px;

    border: 1px solid rgba(30, 45, 60, 0.16);
    border-radius: 18px;

    background: rgba(255, 255, 255, 0.97);

    box-shadow:
        0 18px 50px rgba(20, 30, 40, 0.15),
        0 3px 12px rgba(20, 30, 40, 0.06);
}


/* =========================================================
   Dialog positioning
   Floating navigation bar を考慮
   ========================================================= */

/*
 * floating-nav:
 *   height: 68px
 *   bottom: 14px + safe-area
 *
 * さらに 16px の余白を確保する。
 *
 * これによりダイアログの中央位置を、
 * 画面全体ではなく「ナビを除いた領域」の中央にする。
 */

.q-dialog__inner {
    padding-top: 0;
    padding-bottom:
        calc(
            68px
            + 14px
            + env(safe-area-inset-bottom)
            + 16px
        );
}


/* =========================================================
   Dark mode
   ========================================================= */

.body--dark .weather-dialog {
    border-color: rgba(255, 255, 255, 0.10);

    background: rgba(30, 34, 39, 0.97);

    box-shadow:
        0 18px 50px rgba(0, 0, 0, 0.40),
        0 3px 12px rgba(0, 0, 0, 0.22);
}


/* ---------------------------------------------------------
   Header
   --------------------------------------------------------- */

.dialog-eyebrow {
    margin-bottom: 2px;

    color: #8b969f;

    font-size: 10px;
    font-weight: 700;

    letter-spacing: 0.16em;
}

.body--dark .dialog-eyebrow {
    color: #8f9aa3;
}


.dialog-title {
    color: #182635;

    font-size: 25px;
    font-weight: 800;

    line-height: 1.25;
    letter-spacing: -0.025em;
}

.body--dark .dialog-title {
    color: #edf1f4;
}


.dialog-separator {
    margin: 9px 0 20px;

    background: rgba(30, 45, 60, 0.14);
}

.body--dark .dialog-separator {
    background: rgba(255, 255, 255, 0.12);
}


/* ---------------------------------------------------------
   Information
   --------------------------------------------------------- */

.dialog-info {
    gap: 5px;
}


.dialog-section-label {
    margin-bottom: 1px;

    color: #8b969f;

    font-size: 9px;
    font-weight: 700;

    letter-spacing: 0.16em;
}

.body--dark .dialog-section-label {
    color: #929da5;
}


.dialog-time {
    color: #172738;

    font-size: 18px;
    font-weight: 700;

    line-height: 1.35;
}

.body--dark .dialog-time {
    color: #e7edf1;
}


.dialog-age {
    color: #008c9a;

    font-size: 13px;
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

    margin-top: 14px;
    padding: 10px 13px;

    gap: 8px;
    align-items: center;

    border: 1px solid rgba(30, 45, 60, 0.10);
    border-radius: 9px;

    background: rgba(245, 247, 249, 0.8);
}

.body--dark .dialog-file-row {
    border-color: rgba(255, 255, 255, 0.09);

    background: rgba(255, 255, 255, 0.045);
}


.dialog-file-icon {
    color: #8c99a3;

    font-size: 17px;
}

.body--dark .dialog-file-icon {
    color: #9ba6ae;
}


.dialog-filename {
    overflow: hidden;

    color: #687681;

    font-family: monospace;
    font-size: 11px;

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

    margin-top: 2px;

    justify-content: flex-end;
    align-items: center;

    gap: 4px;

    flex-wrap: wrap;
}


.dialog-button,
.dialog-cancel-button {
    min-height: 38px;

    border-radius: 9px;

    color: #43515d;

    font-size: 13px;
    font-weight: 600;
}

.body--dark .dialog-button,
.body--dark .dialog-cancel-button {
    color: #c2cbd1;
}


.dialog-primary-button {
    min-height: 38px;

    padding: 0 16px;

    border-radius: 9px;

    background: #147bd1 !important;

    color: white !important;

    font-size: 13px;
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

    .q-dialog__inner {
        padding-left: 12px;
        padding-right: 12px;

        padding-bottom:
            calc(
                68px
                + 14px
                + env(safe-area-inset-bottom)
                + 14px
            );
    }


    .weather-dialog {
        width: 100%;
        max-width: none;

        padding: 21px 20px 18px;

        border-radius: 16px;
    }


    .dialog-title {
        font-size: 22px;
    }


    .dialog-separator {
        margin: 8px 0 18px;
    }


    .dialog-actions {
        justify-content: stretch;
    }


    .dialog-primary-button,
    .dialog-cancel-button,
    .dialog-button {
        min-height: 38px;
    }
}


/* =========================================================
   Very short screens
   ========================================================= */

@media (max-height: 600px) {

    .weather-dialog {
        padding-top: 18px;
        padding-bottom: 16px;
    }


    .dialog-separator {
        margin-bottom: 14px;
    }


    .dialog-file-row {
        margin-top: 10px;
        padding-top: 8px;
        padding-bottom: 8px;
    }
}

"""