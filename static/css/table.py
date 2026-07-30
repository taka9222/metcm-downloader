def css_table():
    return """

.glass-table {
    border-radius: 18px;
    overflow: hidden;
    background: rgba(235, 237, 240, .72) !important;
    border: 1px solid rgba(110, 115, 122, .28) !important;
    backdrop-filter: blur(20px) saturate(120%);
    -webkit-backdrop-filter: blur(20px) saturate(120%);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.10);
}


/* テーブル内部は透明にして、外側のガラスを見せる */
.glass-table .q-table__container,
.glass-table .q-table__middle {
    background: transparent !important;
}


/* Header */
.glass-table thead tr {
    background: rgba(220, 223, 227, .82);
}

.glass-table thead th {
    background: transparent !important;
    font-weight: 600;
    border-bottom: 1px solid rgba(100, 105, 112, .22) !important;
}

/* Body */
.glass-table tbody tr {
    background: rgba(255, 255, 255, .38);
    transition: background .15s ease;
}

.glass-table tbody td {
    border-color:
        rgba(100, 105, 112, .14) !important;
}

/* Hover */
.glass-table tbody tr:hover {
    background: rgba(220, 223, 227, .55);
}

/* Dark Mode */
.body--dark .glass-table {
    background: rgba(38, 39, 41, .55) !important;
    border-color: rgba(255, 255, 255, .15) !important;
}

.body--dark .glass-table thead tr {
    background: rgba(255, 255, 255, .09);
}

.body--dark .glass-table tbody tr {
    background: rgba(255, 255, 255, .025);
}

.body--dark .glass-table tbody tr:hover {
    background: rgba(255, 255, 255, .08);
}

.body--dark .glass-table tbody td {
    border-color: rgba(255, 255, 255, .08) !important;
}
    
"""