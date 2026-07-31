def css_map():
    return """

/* =========================================================
   Map Page
   ========================================================= */

.map-page {
    gap: 0 !important;
}

/* =========================================================
   Map Wrapper
   ========================================================= */

.map-wrapper {
    position: relative;
    width: 100%;
    height: min(68vh, 620px);
    margin-top: 28px;
    overflow: hidden;
    border-radius: 22px;
    border: 1px solid rgba(110, 118, 126, 0.28);
    background: #e8ecef;
    box-shadow: 0 10px 32px rgba(25, 35, 45, 0.10);
}

/* Leaflet本体 */
.map-view {
    width: 100%;
    height: 100%;
    border-radius: 22px;
}

/* =========================================================
   Map Overlay
   ========================================================= */

.map-overlay {
    position: absolute;
    z-index: 1000;
    right: 18px;
    top: 18px;
    left: auto;
    padding: 10px 15px;
    border-radius: 12px;
    background: rgba(255, 255, 255, 0.78);
    border: 1px solid rgba(110, 118, 126, 0.20);
    backdrop-filter: blur(18px) saturate(120%);
    -webkit-backdrop-filter: blur(18px) saturate(120%);
    box-shadow: 0 5px 18px rgba(20, 30, 40, 0.10);
}

.map-overlay-label {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 0.20em;
    color: #8c949c;
}

.map-overlay-coordinate {
    margin-top: 2px;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.03em;
    color: #1c2937;
}

/* =========================================================
   Information Card
   ========================================================= */

.map-info-card {
    width: 100%;
    margin-top: 18px;
    padding: 20px 22px !important;
    border-radius: 20px !important;
    background: rgba(248, 249, 250, 0.78) !important;
    border: 1px solid rgba(110, 118, 126, 0.25) !important;
    box-shadow: 0 8px 28px rgba(25, 35, 45, 0.07);
    backdrop-filter: blur(20px) saturate(115%);
    -webkit-backdrop-filter: blur(20px) saturate(115%);
}

/* =========================================================
   Information Header
   ========================================================= */

.map-info-header {
    align-items: center;
    gap: 12px;
}

.map-location-icon {
    font-size: 28px;
    color: #26858d;
}

.map-info-eyebrow {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 0.20em;
    color: #9299a1;
}

.map-info-title {
    margin-top: 2px;
    font-size: 19px;
    font-weight: 600;
    color: #1b2735;
}

/* =========================================================
   Separator
   ========================================================= */

.map-info-separator {
    margin: 17px 0 15px 0;
    background: rgba(100, 108, 116, 0.16) !important;
}

/* =========================================================
   Coordinates
   ========================================================= */

.map-coordinate-row {
    width: 100%;
    gap: 0;
}

.map-coordinate-item {
    flex: 1;
    gap: 2px;
}

.map-coordinate-item + .map-coordinate-item {
    border-left: 1px solid rgba(100, 108, 116, 0.14);
    padding-left: 20px;
}

.map-coordinate-label {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 0.16em;
    color: #969da4;
}

.map-coordinate-value {
    font-size: 16px;
    font-weight: 500;
    color: #273443;
}

/* =========================================================
   Bottom Space
   ========================================================= */

.map-bottom-space {
    height: calc(110px + env(safe-area-inset-bottom));
}

/* =========================================================
   Dark Mode
   ========================================================= */

.body--dark .map-wrapper {
    background: #202326;
    border-color: rgba(255, 255, 255, 0.13);
    box-shadow: 0 10px 35px rgba(0, 0, 0, 0.30);
}

.body--dark .map-overlay {
    background: rgba(30, 33, 36, 0.78);
    border-color: rgba(255, 255, 255, 0.13);
}

.body--dark .map-overlay-label,
.body--dark .map-info-eyebrow,
.body--dark .map-coordinate-label {
    color: #929aa2;
}

.body--dark .map-overlay-coordinate {
    color: #f1f3f5;
}

.body--dark .map-info-card {
    background: rgba(32, 35, 38, 0.72) !important;
    border-color: rgba(255, 255, 255, 0.14) !important;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.25);
}

.body--dark .map-info-title,
.body--dark .map-coordinate-value {
    color: #f0f2f4;
}


.body--dark .map-info-separator {
    background: rgba(255, 255, 255, 0.10) !important;
}


.body--dark .map-coordinate-item + .map-coordinate-item {
    border-color: rgba(255, 255, 255, 0.10);
}


/* =========================================================
   Mobile
   ========================================================= */

@media (max-width: 600px) {

    .map-wrapper {
        height: 62vh;
        margin-top: 25px;
        border-radius: 19px;
    }

    .map-view {
        border-radius: 19px;
    }

    .map-overlay {
        right: 13px;
        left: auto;
        top: 13px;
        padding: 8px 12px;
    }

    .map-overlay-label {
        font-size: 8px;
    }

    .map-overlay-coordinate {
        font-size: 12px;
    }

    .map-info-card {
        margin-top: 14px;
        padding: 17px 18px !important;
        border-radius: 18px !important;
    }

    .map-info-title {
        font-size: 18px;
    }

    .map-coordinate-value {
        font-size: 15px;
    }

    .map-coordinate-item + .map-coordinate-item {
        padding-left: 15px;
    }
}

"""