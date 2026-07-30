def css_settings():

    return """

/* =========================================================
   Settings
   ========================================================= */

.settings-page {
    gap: 0 !important;
}


/* =========================================================
   Section
   ========================================================= */

.settings-section {
    width: 100%;
    margin-top: 32px;
}

.settings-section-header {
    display: flex;
    align-items: baseline;

    gap: 10px;

    padding: 0 4px 10px 4px;
}


/* English */

.settings-section-eyebrow {
    font-size: 10px;
    font-weight: 700;

    letter-spacing: .22em;

    color: #9299a1;
}


/* Japanese */

.settings-section-title {
    font-size: 19px;
    font-weight: 600;

    color: #1c2632;
}


/* =========================================================
   Settings Card
   ========================================================= */

.settings-card {
    width: 100%;

    overflow: hidden;

    border-radius: 18px;

    background:
        rgba(248, 249, 250, .78);

    border:
        1px solid rgba(110, 118, 126, .25);

    backdrop-filter:
        blur(20px) saturate(115%);

    -webkit-backdrop-filter:
        blur(20px) saturate(115%);

    box-shadow:
        0 7px 25px rgba(25, 35, 45, .06);
}


/* =========================================================
   Table
   ========================================================= */

.settings-table {
    width: 100% !important;

    background: transparent !important;

    box-shadow: none !important;
}

.settings-table thead {
    display: none;
}

.settings-table .q-table__middle {
    background: transparent;
}

.settings-table table {
    width: 100%;
}


/* =========================================================
   Table Row
   ========================================================= */

.settings-table tbody tr {
    height: 68px;

    background: transparent;

    cursor: pointer;

    transition:
        background .15s ease;
}


.settings-table tbody tr:hover {
    background:
        rgba(225, 229, 233, .55);
}


/* =========================================================
   Row Divider
   ========================================================= */

.settings-table tbody tr + tr td {
    border-top:
        1px solid rgba(100, 108, 116, .13) !important;
}


/* =========================================================
   Cells
   ========================================================= */

.settings-table td {
    height: 68px;

    padding: 0 20px !important;

    border: none !important;

    vertical-align: middle;
}


/* Left */

.settings-table-title-cell {
    width: 100%;
}


/* Right */

.settings-table-value-cell {
    width: 1%;

    white-space: nowrap;

    text-align: right;
}


/* =========================================================
   Title
   ========================================================= */

.settings-table-title {
    display: flex;
    align-items: center;

    gap: 14px;

    font-size: 16px;
    font-weight: 500;

    color: #202a35;

    white-space: nowrap;
}


/* =========================================================
   Icon
   ========================================================= */

.settings-table-icon {
    width: 28px;

    font-size: 20px;

    color: #5f6871;
}


/* =========================================================
   Value
   ========================================================= */

.settings-table-value {
    display: flex;
    align-items: center;
    justify-content: flex-end;

    gap: 6px;

    font-size: 12px;

    color: #858d95;

    white-space: nowrap;
}


/* =========================================================
   Arrow
   ========================================================= */

.settings-table-arrow {
    font-size: 20px;

    color: #9aa1a8;
}


/* =========================================================
   Setting Dialog
   ========================================================= */

.setting-dialog {
    width: min(
        420px,
        calc(100vw - 32px)
    );

    max-width: 420px;

    padding: 0;

    overflow: hidden;

    border-radius: 20px;

    background:
        rgba(248, 249, 250, .94);

    backdrop-filter:
        blur(25px) saturate(120%);

    -webkit-backdrop-filter:
        blur(25px) saturate(120%);

    box-shadow:
        0 20px 60px rgba(20, 25, 30, .18);
}


/* Dialog Header */

.setting-dialog-header {
    width: 100%;

    min-height: 58px;

    padding: 0 12px 0 20px;

    box-sizing: border-box;

    align-items: center;

    justify-content: space-between;

    border-bottom:
        1px solid rgba(100, 108, 116, .13);
}


.setting-dialog-title {
    font-size: 18px;
    font-weight: 600;

    color: #202a35;
}


/* =========================================================
   Options
   ========================================================= */

.setting-options {
    width: 100%;

    padding: 8px 0;
}


.setting-option {
    width: 100%;
    min-height: 52px;

    padding: 0 20px;

    box-sizing: border-box;

    display: flex;
    align-items: center;
    justify-content: space-between;

    cursor: pointer;

    transition:
        background .15s ease;
}


.setting-option:hover {
    background:
        rgba(225, 229, 233, .55);
}


.setting-option-label {
    font-size: 15px;

    color: #202a35;
}


.setting-option-check {
    font-size: 20px;

    color: #5f6871;
}


/* =========================================================
   Dark Mode
   ========================================================= */

.body--dark .settings-section-title {
    color: #f0f2f4;
}


.body--dark .settings-card {
    background:
        rgba(32, 35, 38, .72);

    border-color:
        rgba(255, 255, 255, .14);

    box-shadow:
        0 8px 30px rgba(0, 0, 0, .25);
}


.body--dark .settings-table tbody tr:hover {
    background:
        rgba(255, 255, 255, .06);
}


.body--dark .settings-table tbody tr + tr td {
    border-color:
        rgba(255, 255, 255, .08) !important;
}


.body--dark .settings-table-icon {
    color: #aeb5bb;
}


.body--dark .settings-table-title {
    color: #f0f2f4;
}


.body--dark .settings-table-value {
    color: #929aa2;
}


.body--dark .settings-table-arrow {
    color: #777f87;
}


/* =========================================================
   Dialog - Dark Mode
   ========================================================= */

.body--dark .setting-dialog {
    background:
        rgba(32, 35, 38, .94);

    box-shadow:
        0 20px 60px rgba(0, 0, 0, .45);
}


.body--dark .setting-dialog-header {
    border-color:
        rgba(255, 255, 255, .10);
}


.body--dark .setting-dialog-title {
    color: #f0f2f4;
}


.body--dark .setting-option:hover {
    background:
        rgba(255, 255, 255, .06);
}


.body--dark .setting-option-label {
    color: #f0f2f4;
}


.body--dark .setting-option-check {
    color: #aeb5bb;
}


/* =========================================================
   Mobile
   ========================================================= */

@media (max-width: 600px) {

    .settings-section {
        margin-top: 28px;
    }

    .settings-section-header {
        padding-bottom: 9px;
    }

    .settings-section-title {
        font-size: 18px;
    }


    .settings-table tbody tr {
        height: 64px;
    }


    .settings-table td {
        height: 64px;

        padding: 0 17px !important;
    }


    .settings-table-title {
        gap: 12px;

        font-size: 16px;
    }


    .settings-table-icon {
        width: 26px;

        font-size: 19px;
    }


    .settings-table-value {
        font-size: 11px;
    }


    .settings-table-arrow {
        font-size: 19px;
    }


    .setting-dialog {
        width: calc(100vw - 24px);

        border-radius: 18px;
    }


    .setting-option {
        min-height: 50px;

        padding: 0 18px;
    }

}

"""