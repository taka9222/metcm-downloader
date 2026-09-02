def css_home_dashboard():
    return """

/* =========================================================
   Home Page
   ========================================================= */

.home-page {
    gap: 0 !important;
}

/* =========================================================
   Dashboard Section Header
   ========================================================= */

.dashboard-section-header {
    width: 100%;
    margin-top: 30px;
    margin-bottom: 12px;
    gap: 2px !important;
}

.dashboard-section-eyebrow {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 0.28em;
    color: rgba(50, 65, 78, 0.46);
}

.body--dark .dashboard-section-eyebrow {
    color: rgba(220, 230, 238, 0.42);
}

.dashboard-section-title {
    font-size: 17px;
    font-weight: 600;
    letter-spacing: 0.01em;
    color: #263442;
}

.body--dark .dashboard-section-title {
    color: #e7edf1;
}

.dashboard-section-line {
    width: 100%;
    height: 1px;
    margin-top: 7px;
    background:
        linear-gradient(
            90deg,
            rgba(50, 75, 90, 0.25),
            rgba(50, 75, 90, 0.06),
            transparent
        );
}

.body--dark .dashboard-section-line {
    background:
        linear-gradient(
            90deg,
            rgba(210, 225, 235, 0.22),
            rgba(210, 225, 235, 0.05),
            transparent
        );
}


/* =========================================================
   Location Card
   ========================================================= */

.location-card {
    margin-bottom: 14px;
}

/* =========================================================
   Recent Badge
   ========================================================= */

.location-recent-badge {
    position: absolute;
    top: 24px;
    right: 24px;
    padding: 5px 9px;
    border: 1px solid rgba(38, 120, 125, 0.25);
    border-radius: 6px;
    background: rgba(255, 255, 255, 0.28);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    font-size: 8px;
    font-weight: 700;
    letter-spacing: 0.18em;
    color: #26787d;
}

.body--dark .location-recent-badge {
    background: rgba(25, 35, 42, 0.45);
    border-color: rgba(95, 190, 195, 0.28);
    color: #6bc1c4;
}


/* =========================================================
   Weather Card
   ========================================================= */

.weather-card {
    position: relative;
    padding: 22px !important;
    border-radius: 16px;
    background: rgba(245, 248, 250, 0.88);
    border: 1px solid rgba(45, 65, 80, 0.13);
    box-shadow: 0 8px 28px rgba(0, 0, 0, 0.07);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    transition:
        background 0.25s ease,
        border-color 0.25s ease;
}

.body--dark .weather-card {
    background: rgba(22, 28, 34, 0.88);
    border-color: rgba(255, 255, 255, 0.13);
    box-shadow: 0 10px 32px rgba(0, 0, 0, 0.28);
}


/* =========================================================
   Weather Header
   ========================================================= */

.weather-card-header {
    width: 100%;
    align-items: center;
    justify-content: space-between;
}

.weather-location {
    font-size: 18px;
    font-weight: 650;
    color: #263542;
}

.body--dark .weather-location {
    color: #e8eef2;
}

.weather-subtitle {
    margin-top: 3px;
    font-size: 10px;
    letter-spacing: 0.08em;
    color: rgba(60, 75, 88, 0.48);
}

.body--dark .weather-subtitle {
    color: rgba(215, 225, 232, 0.42);
}

.weather-live {
    padding: 3px 7px;
    border-radius: 5px;
    background: rgba(50, 135, 140, 0.10);
    color: #277c80;
    font-size: 8px;
    font-weight: 700;
    letter-spacing: 0.14em;
}

.body--dark .weather-live {
    background: rgba(90, 190, 195, 0.10);
    color: #69c3c5;
}

.weather-icon {
    font-size: 32px;
    color: rgba(65, 85, 98, 0.50);
}

.body--dark .weather-icon {
    color: rgba(215, 225, 232, 0.50);
}

/* =========================================================
   Weather Divider
   ========================================================= */

.weather-divider {
    width: 100%;
    height: 1px;
    margin: 18px 0;
    background: rgba(60, 75, 88, 0.10);
}

.body--dark .weather-divider {
    background: rgba(255, 255, 255, 0.10);
}

/* =========================================================
   Weather Metrics
   ========================================================= */

.weather-metrics {
    width: 100%;
    display: flex;
}

.weather-metric {
    flex: 1;
    align-items: center;
    padding: 4px 8px;
}

.weather-metric + .weather-metric {
    border-left: 1px solid rgba(60, 75, 88, 0.10);
}

.body--dark .weather-metric + .weather-metric {
    border-left-color: rgba(255, 255, 255, 0.10);
}

.weather-metric-value {
    font-size: 27px;
    line-height: 1;
    font-weight: 500;
    font-variant-numeric: tabular-nums;
    color: #273744;
}

.body--dark .weather-metric-value {
    color: #e8eef2;
}

.weather-metric-unit {
    font-size: 11px;
    font-weight: 500;
    color: rgba(60, 75, 88, 0.52);
}

.body--dark .weather-metric-unit {
    color: rgba(215, 225, 232, 0.50);
}

.weather-metric-label {
    margin-top: 7px;
    font-size: 8px;
    font-weight: 700;
    letter-spacing: 0.16em;
    color: rgba(60, 75, 88, 0.43);
}

.body--dark .weather-metric-label {
    color: rgba(215, 225, 232, 0.38);
}

/* =========================================================
   Weather Footer
   ========================================================= */

.weather-footer {
    width: 100%;
    margin-top: 20px;
    align-items: center;
    justify-content: space-between;
}

.weather-source {
    font-size: 9px;
    letter-spacing: 0.05em;
    color: rgba(60, 75, 88, 0.42);
}

.body--dark .weather-source {
    color: rgba(215, 225, 232, 0.36);
}

.weather-refresh-button {
    min-height: 38px;
    padding: 0 15px !important;
    border-radius: 8px;
    background: rgba(55, 125, 130, 0.10);
    color: #26787d;
    border: 1px solid rgba(55, 125, 130, 0.18);
    box-shadow: none;
}

.body--dark .weather-refresh-button {
    background: rgba(90, 180, 185, 0.10);
    border-color: rgba(90, 180, 185, 0.20);
    color: #6bc1c4;
}

.weather-refresh-button:hover {
    background: rgba(55, 125, 130, 0.17);
}

.body--dark .weather-refresh-button:hover {
    background: rgba(90, 180, 185, 0.16);
}

/* =========================================================
   Atmospheric Profile
   ========================================================= */

.altitude-card {
    padding: 22px !important;
    border-radius: 16px;
    background: rgba(245, 248, 250, 0.88);
    border: 1px solid rgba(45, 65, 80, 0.13);
    box-shadow: 0 8px 28px rgba(0, 0, 0, 0.07);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
}

.body--dark .altitude-card {
    background: rgba(22, 28, 34, 0.88);
    border-color: rgba(255, 255, 255, 0.13);
    box-shadow: 0 10px 32px rgba(0, 0, 0, 0.28);
}

/* =========================================================
   Atmospheric Header
   ========================================================= */

.altitude-card-header {
    width: 100%;
    align-items: center;
    justify-content: space-between;
}

.altitude-eyebrow {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 0.22em;
    color: rgba(50, 65, 78, 0.45);
}

.body--dark .altitude-eyebrow {
    color: rgba(220, 230, 238, 0.40);
}

.altitude-title {
    margin-top: 3px;
    font-size: 18px;
    font-weight: 650;
    color: #263542;
}

.body--dark .altitude-title {
    color: #e8eef2;
}

.altitude-icon {
    font-size: 29px;
    color: rgba(65, 85, 98, 0.46);
}

.body--dark .altitude-icon {
    color: rgba(215, 225, 232, 0.46);
}

.altitude-description {
    margin-top: 16px;
    font-size: 12px;
    color: rgba(60, 75, 88, 0.58);
}

.body--dark .altitude-description {
    color: rgba(215, 225, 232, 0.52);
}

/* =========================================================
   Altitude Selector
   ========================================================= */

.altitude-selector-row {
    width: 100%;
    margin-top: 18px;
    align-items: flex-end;
}

.altitude-selector {
    flex: 1;

    gap: 4px !important;
}

.altitude-selector-label {
    font-size: 8px;
    font-weight: 700;
    letter-spacing: 0.18em;
    color: rgba(60, 75, 88, 0.45);
}

.body--dark .altitude-selector-label {
    color: rgba(215, 225, 232, 0.40);
}

.altitude-unit {
    padding-bottom: 10px;
    padding-left: 8px;
    font-size: 13px;
    color: rgba(60, 75, 88, 0.55);
}

.body--dark .altitude-unit {
    color: rgba(215, 225, 232, 0.52);
}

/* =========================================================
   Altitude Action
   ========================================================= */

.altitude-action-button {
    width: 100%;
    min-height: 44px;
    margin-top: 16px;
    border-radius: 9px;
    background: rgba(45, 110, 115, 0.10);
    border: 1px solid rgba(45, 110, 115, 0.18);
    color: #26787d;
    box-shadow: none;
}

.body--dark .altitude-action-button {
    background: rgba(85, 175, 180, 0.10);
    border-color: rgba(85, 175, 180, 0.20);
    color: #6bc1c4;
}

.altitude-action-button:hover {
    background: rgba(45, 110, 115, 0.16);
}

.body--dark .altitude-action-button:hover {
    background: rgba(85, 175, 180, 0.16);
}


/* =========================================================
   Mobile
   ========================================================= */

@media (max-width: 600px) {

    .dashboard-section-header {
        margin-top: 24px;
    }

    .location-card {
        min-height: 245px;
    }

    .location-card-content {
        min-height: 245px;
        padding: 20px;
    }

    .location-title {
        font-size: 23px;
    }

    .location-recent-badge {
        top: 20px;
        right: 20px;
    }

    .weather-card,
    .altitude-card {
        padding: 18px !important;
    }

    .weather-metric-value {
        font-size: 22px;
    }

    .weather-metric-label {
        font-size: 7px;
        letter-spacing: 0.10em;
    }

    .weather-footer {
        align-items: flex-start;
        flex-direction: column;
        gap: 12px;
    }

    .weather-refresh-button {
        width: 100%;
    }
}

"""