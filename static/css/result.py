def css_result():
    return """

/* =========================================================
   Atmospheric Profile Result Page
   ========================================================= */

.result-page {
    width: 100%;
}


/* ---------------------------------------------------------
   Result information
   --------------------------------------------------------- */

.result-info-card {
    width: 100%;
    padding: 28px 32px 24px;

    border: 1px solid rgba(30, 45, 60, 0.12);
    border-radius: 18px;

    background: rgba(255, 255, 255, 0.97);

    box-shadow:
        0 12px 36px rgba(20, 30, 40, 0.10),
        0 3px 12px rgba(20, 30, 40, 0.04);
}


/* Dark mode */
.body--dark .result-info-card {
    border-color: rgba(255, 255, 255, 0.10);

    background: rgba(30, 34, 39, 0.96);

    box-shadow:
        0 12px 36px rgba(0, 0, 0, 0.28),
        0 3px 12px rgba(0, 0, 0, 0.18);
}


.atmosphere-meta {
    gap: 24px;
    margin-bottom: 2px;
}


.atmosphere-location {
    color: #008c9a;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.04em;
}


/* ---------------------------------------------------------
   Display format
   --------------------------------------------------------- */

.result-format-row {
    width: 100%;
    align-items: center;
    justify-content: flex-end;
    gap: 12px;
    margin-top: 24px;
}


.result-format-label {
    color: #7d8992;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 0.08em;
}


.body--dark .result-format-label {
    color: #9ba5ad;
}


.result-format-select {
    min-width: 180px;
}


.dialog-copy-button {
    min-width: 110px;
}


/* ---------------------------------------------------------
   Atmospheric table
   --------------------------------------------------------- */

.result-table-container {
    width: 100%;
    overflow-x: auto;
}


.atmosphere-table {
    width: 100%;
    min-width: max-content;
    margin-top: 18px;

    border: 1px solid rgba(30, 45, 60, 0.12);
    border-radius: 12px;
    overflow: hidden;

    /* Quasar の影を無効化 */
    box-shadow: none !important;

    background: #ffffff;
}


/* Dark mode */
.body--dark .atmosphere-table {
    border-color: rgba(255, 255, 255, 0.10);
    background: #1e2227;
}


.atmosphere-table .q-table__container {
    border-radius: inherit;
    box-shadow: none !important;
    background: #ffffff;
}


.body--dark .atmosphere-table .q-table__container {
    background: #1e2227;
}


.atmosphere-table .q-table__middle {
    border-radius: inherit;
}


.atmosphere-table .q-table {
    width: 100%;
    box-shadow: none !important;
}


/* ---------------------------------------------------------
   Header
   --------------------------------------------------------- */

.atmosphere-table thead tr {
    background: rgba(240, 243, 246, 0.9);
}


.body--dark .atmosphere-table thead tr {
    background: rgba(255, 255, 255, 0.055);
}


.atmosphere-table th {
    height: 52px;

    color: #7d8992 !important;
    font-size: 10px !important;
    font-weight: 800 !important;
    letter-spacing: 0.08em;

    /* \n の位置で必ず改行 */
    white-space: pre-line !important;
    line-height: 1.25 !important;

    vertical-align: middle;
}


.body--dark .atmosphere-table th {
    color: #9ba5ad !important;
}


/* ---------------------------------------------------------
   Body
   --------------------------------------------------------- */

.atmosphere-table td {
    color: #263746 !important;
    font-size: 12px !important;
    font-variant-numeric: tabular-nums;

    white-space: nowrap;
}


.body--dark .atmosphere-table td {
    color: #d7dde2 !important;
}


.atmosphere-table tbody tr {
    border-bottom: 1px solid rgba(30, 45, 60, 0.08);
}


.body--dark .atmosphere-table tbody tr {
    border-bottom-color: rgba(255, 255, 255, 0.07);
}


.atmosphere-table tbody tr:hover {
    background: rgba(20, 125, 209, 0.04);
}


.body--dark .atmosphere-table tbody tr:hover {
    background: rgba(80, 170, 230, 0.08);
}


/* ---------------------------------------------------------
   Mobile
   --------------------------------------------------------- */

@media (max-width: 700px) {

    .result-info-card {
        padding: 22px 20px 20px;
    }


    .result-format-row {
        justify-content: space-between;
        align-items: center;
    }


    .result-format-select {
        min-width: 160px;
    }


    .atmosphere-table {
        margin-top: 14px;
    }
}

"""