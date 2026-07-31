def css_map():
    return """

/* =========================================================
   Full Screen Map Page
   ========================================================= */

.map-page {
    position: fixed !important;
    inset: 0 !important;
    width: 100vw !important;
    height: 100dvh !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden;
    z-index: 0;
}


/* =========================================================
   Map
   ========================================================= */

.map-view {
    position: absolute !important;
    inset: 0 !important;
    width: 100% !important;
    height: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
    z-index: 0;
}

.leaflet-control-zoom {
    margin-top: 70px !important;
    margin-right: 14px !important;
}

/* =========================================================
   Back Button
   ========================================================= */

.map-back-button {
    position: absolute;
    top: calc(14px + env(safe-area-inset-top));
    left: 14px;
    z-index: 1000;
    width: 42px;
    height: 42px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid rgba(255, 255, 255, 0.35);
    border-radius: 13px;
    background: rgba(255, 255, 255, 0.68);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    box-shadow: 0 6px 24px rgba(0, 0, 0, 0.14);
}


/* =========================================================
   Current Location Overlay
   ========================================================= */

.map-overlay {
    position: absolute;
    top: calc(14px + env(safe-area-inset-top));
    left: 68px;
    z-index: 1000;
    padding: 9px 13px;
    border: 1px solid rgba(255, 255, 255, 0.30);
    border-radius: 12px;
    background: rgba(255, 255, 255, 0.60);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    box-shadow: 0 6px 24px rgba(0, 0, 0, 0.10);
}


/* =========================================================
   Overlay Text
   ========================================================= */

.map-overlay-label {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 0.14em;
    line-height: 1;
    color: rgba(45, 55, 60, 0.55);
}

.map-overlay-coordinate {
    margin-top: 3px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.03em;
    line-height: 1.1;
    color: rgba(35, 45, 50, 0.82);
}


/* =========================================================
   Location Information
   ========================================================= */

.map-info-card {
    position: absolute;
    left: 16px;
    bottom: calc(16px + env(safe-area-inset-bottom));
    z-index: 1000;
    width: min(340px, calc(100vw - 32px));
    margin: 0 !important;
    padding: 14px 16px !important;
    border: 1px solid rgba(255, 255, 255, 0.35);
    border-radius: 16px;
    background: rgba(255, 255, 255, 0.68);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    box-shadow: 0 10px 35px rgba(0, 0, 0, 0.14);
}


/* =========================================================
   Location Header
   ========================================================= */

.map-info-header {
    align-items: center;
    gap: 10px !important;
}

.map-location-icon {
    font-size: 22px;
    color: rgba(38, 120, 125, 0.82);
}

.map-info-eyebrow {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 0.14em;
    line-height: 1.1;
    color: rgba(45, 55, 60, 0.48);
}

.map-info-title {
    margin-top: 2px;
    font-size: 14px;
    font-weight: 650;
    line-height: 1.2;
}


/* =========================================================
   Separator
   ========================================================= */

.map-info-separator {
    margin: 11px 0 !important;
    opacity: 0.35;
}


/* =========================================================
   Coordinates
   ========================================================= */

.map-coordinate-row {
    width: 100%;
    gap: 28px !important;
}

.map-coordinate-item {
    flex: 1;
    gap: 2px !important;
}

.map-coordinate-label {
    font-size: 8px;
    font-weight: 700;
    letter-spacing: 0.13em;
    color: rgba(45, 55, 60, 0.45);
}

.map-coordinate-value {
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.02em;
    color: rgba(30, 40, 45, 0.88);
}


/* =========================================================
   Dark Mode
   ========================================================= */

.body--dark .map-back-button,
.body--dark .map-overlay,
.body--dark .map-info-card {
    background: rgba(25, 30, 34, 0.70);
    border-color: rgba(255, 255, 255, 0.12);
    box-shadow: 0 10px 35px rgba(0, 0, 0, 0.38);
}

.body--dark .map-overlay-label,
.body--dark .map-info-eyebrow,
.body--dark .map-coordinate-label {
    color: rgba(230, 235, 238, 0.48);
}

.body--dark .map-overlay-coordinate,
.body--dark .map-info-title,
.body--dark .map-coordinate-value {
    color: rgba(240, 244, 246, 0.88);
}


/* =========================================================
   Mobile
   ========================================================= */

@media (max-width: 600px) {
    .map-info-card {
        left: 12px;
        bottom: calc(12px + env(safe-area-inset-bottom));
        width: calc(100vw - 24px);
        padding: 13px 14px !important;
    }

    .map-overlay {
        left: 64px;
    }

    .map-coordinate-row {
        gap: 18px !important;
    }
}

"""