def css_table():
    return """

/* =========================================================
   Range Section
   ========================================================= */

.range-section {
    width: 100%;
    gap: 14px;
    margin-top: 34px;
}

.range-section-title {
    width: 100%;
    align-items: baseline;
    gap: 12px;
    padding-left: 4px;
}

/* 英字ラベル */
.range-section-title > div:first-child {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.22em;
    color: #9299a1;
}

/* 日本語 */
.range-section-title > div:last-child {
    font-size: 21px;
    font-weight: 600;
    letter-spacing: 0.02em;
    color: #1c2633;
}


/* =========================================================
   Table
   ========================================================= */

.glass-table {
    width: 100%;

    border-radius: 20px;
    overflow: hidden;

    background: rgba(248, 249, 250, 0.78) !important;

    border: 1px solid rgba(115, 122, 130, 0.28) !important;

    backdrop-filter: blur(22px) saturate(115%);
    -webkit-backdrop-filter: blur(22px) saturate(115%);

    box-shadow:
        0 8px 28px rgba(25, 35, 45, 0.07);
}


/* Table内部 */
.glass-table .q-table__container,
.glass-table .q-table__middle {
    background: transparent !important;
}


/* =========================================================
   Rows
   ========================================================= */

.glass-table tbody tr {
    min-height: 92px;

    background: rgba(255, 255, 255, 0.45);

    transition:
        background 0.15s ease,
        transform 0.15s ease;
}

.glass-table tbody tr:hover {
    background: rgba(235, 239, 242, 0.72);
}


/* 行の境界 */
.glass-table tbody td {
    border-color:
        rgba(110, 118, 126, 0.16) !important;
}


/* =========================================================
   Location
   ========================================================= */

.range-table-location {
    padding:
        18px 12px
        18px 32px !important;
}

.range-row-content {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}


/* 場所名 */
.range-name {
    color: #172332;

    font-size: 21px;
    font-weight: 500;

    line-height: 1.25;
    letter-spacing: 0.015em;
}


/* 国名 */
.range-country {
    margin-top: 4px;

    color: #2c858d;

    font-size: 13px;
    font-weight: 600;

    letter-spacing: 0.08em;
}


/* 座標 */
.range-coordinates {
    display: flex;
    gap: 14px;

    margin-top: 7px;

    color: #7b838b;

    font-size: 13px;
    font-weight: 400;

    letter-spacing: 0.02em;
}


/* =========================================================
   Menu
   ========================================================= */

.range-menu-cell {
    padding-right: 20px !important;
}

.range-menu-button {
    color: #111 !important;
}


/* =========================================================
   Dark Mode
   ========================================================= */

.body--dark .range-section-title > div:first-child {
    color: #8d969f;
}

.body--dark .range-section-title > div:last-child {
    color: #f0f2f4;
}

.body--dark .glass-table {
    background:
        rgba(32, 35, 38, 0.72) !important;

    border-color:
        rgba(255, 255, 255, 0.14) !important;

    box-shadow:
        0 8px 30px rgba(0, 0, 0, 0.25);
}

.body--dark .glass-table tbody tr {
    background:
        rgba(255, 255, 255, 0.025);
}

.body--dark .glass-table tbody tr:hover {
    background:
        rgba(255, 255, 255, 0.07);
}

.body--dark .glass-table tbody td {
    border-color:
        rgba(255, 255, 255, 0.08) !important;
}

.body--dark .range-name {
    color: #f0f2f4;
}

.body--dark .range-country {
    color: #63aeb4;
}

.body--dark .range-coordinates {
    color: #929aa2;
}

.body--dark .range-menu-button {
    color: #f2f2f2 !important;
}


/* =========================================================
   Mobile
   ========================================================= */

@media (max-width: 600px) {

    .range-section {
        margin-top: 30px;
        gap: 12px;
    }

    .range-section-title {
        gap: 9px;
    }

    .range-section-title > div:first-child {
        font-size: 10px;
    }

    .range-section-title > div:last-child {
        font-size: 20px;
    }

    .glass-table {
        border-radius: 18px;
    }

    .range-table-location {
        padding:
            18px 8px
            18px 24px !important;
    }

    .range-name {
        font-size: 19px;
    }

    .range-country {
        font-size: 12px;
    }

    .range-coordinates {
        gap: 10px;
        font-size: 12px;
    }

    .range-menu-cell {
        padding-right: 12px !important;
    }
}

"""