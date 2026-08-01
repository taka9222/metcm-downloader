def css_search_result():
    return """

/* =========================================================
   FNL Search Results
   ========================================================= */

.fnl-results {
    width: 100%;
    gap: 0;
    border: 1px solid rgba(30, 45, 60, 0.12);
    border-radius: 14px;
    overflow: hidden;
}

.fnl-result-row {
    width: 100%;
    min-height: 76px;
    padding: 12px 14px;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid rgba(30, 45, 60, 0.10);
}

.fnl-result-row:last-child {
    border-bottom: none;
}

.fnl-result-info {
    flex: 1;
    gap: 2px;
}

.fnl-result-time {
    color: #172738;
    font-size: 16px;
    font-weight: 800;
}

.fnl-result-filename {
    color: #8a959d;
    font-family: monospace;
    font-size: 10px;
}

.fnl-available,
.fnl-unavailable {
    margin: 0 10px;
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 0.12em;
}

.fnl-available {
    color: #008c9a;
}

.fnl-unavailable {
    color: #a0a8ae;
}

"""
