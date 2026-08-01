def css_result():
    return """

/* =========================================================
   Atmospheric Profile Dialog
   ========================================================= */

.atmosphere-dialog {
    width: min(1100px, calc(100vw - 32px));
    max-width: 1100px;
    max-height: calc(100vh - 48px);
    padding: 32px 36px 28px;
    border: 1px solid rgba(30, 45, 60, 0.16);
    border-radius: 22px;
    background: rgba(255, 255, 255, 0.97);
    box-shadow:
        0 20px 60px rgba(20, 30, 40, 0.16),
        0 4px 16px rgba(20, 30, 40, 0.06);
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

.atmosphere-table {
    width: 100%;
    margin-top: 18px;
    border: 1px solid rgba(30, 45, 60, 0.12);
    border-radius: 12px;
    overflow: hidden;
}

.atmosphere-table thead tr {
    background: rgba(240, 243, 246, 0.9);
}

.atmosphere-table th {
    color: #7d8992 !important;
    font-size: 10px !important;
    font-weight: 800 !important;
    letter-spacing: 0.08em;
    white-space: nowrap;
}

.atmosphere-table td {
    color: #263746 !important;
    font-size: 12px !important;
    font-variant-numeric: tabular-nums;
    white-space: nowrap;
}

.atmosphere-table tbody tr {
    border-bottom: 1px solid rgba(30, 45, 60, 0.08);
}

.atmosphere-table tbody tr:hover {
    background: rgba(20, 125, 209, 0.04);
}

"""
