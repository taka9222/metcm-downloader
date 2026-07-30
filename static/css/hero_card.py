def css_hero_card():
    return """

/* =========================================================
   Location Card
   ========================================================= */

.location-card {
    position: relative;
    overflow: hidden;

    min-height: 260px;
    padding: 0 !important;

    border-radius: 18px;

    /* Light */
    background: #eef1f3;

    /* Card outline */
    border: 1px solid rgba(40, 55, 70, 0.14);

    box-shadow:
        0 8px 30px rgba(0, 0, 0, 0.10);

    transition:
        background 0.25s ease,
        border-color 0.25s ease,
        box-shadow 0.25s ease;
}

.location-card-image,
.location-card-fade,
.location-card-hud {
    border-radius: inherit;
}


/* =========================================================
   Dark mode - Card
   ========================================================= */

.body--dark .location-card {
    background: #151a1f;

    border-color: rgba(255, 255, 255, 0.16);

    box-shadow:
        0 10px 35px rgba(0, 0, 0, 0.35);
}


/* =========================================================
   Background image
   ========================================================= */

.location-card-image {
    position: absolute;
    inset: 0;

    width: 100%;
    height: 100%;

    object-fit: cover;
    object-position: 65% center;

    z-index: 0;
}


/* =========================================================
   Light fade
   ========================================================= */

.location-card-fade {
    position: absolute;
    inset: 0;

    z-index: 1;
    pointer-events: none;

    background:
        linear-gradient(
            120deg,
            rgba(248, 250, 252, 1.00) 0%,
            rgba(248, 250, 252, 1.00) 30%,
            rgba(248, 250, 252, 0.96) 40%,
            rgba(248, 250, 252, 0.72) 50%,
            rgba(248, 250, 252, 0.25) 61%,
            rgba(248, 250, 252, 0.00) 75%
        ),

        linear-gradient(
            135deg,
            rgba(255, 255, 255, 0.45) 0%,
            rgba(255, 255, 255, 0.00) 55%
        );
}


/* =========================================================
   Dark mode - fade
   ========================================================= */

.body--dark .location-card-fade {
    background:
        linear-gradient(
            120deg,
            rgba(18, 23, 28, 0.98) 0%,
            rgba(18, 23, 28, 0.97) 30%,
            rgba(18, 23, 28, 0.91) 40%,
            rgba(18, 23, 28, 0.68) 50%,
            rgba(18, 23, 28, 0.28) 61%,
            rgba(18, 23, 28, 0.00) 78%
        ),

        linear-gradient(
            135deg,
            rgba(255, 255, 255, 0.08) 0%,
            rgba(255, 255, 255, 0.00) 55%
        );
}


/* =========================================================
   HUD overlay
   ========================================================= */

.location-card-hud {
    position: absolute;
    inset: 0;

    z-index: 2;
    pointer-events: none;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.30) 0%,
            transparent 30%
        );

    border: 1px solid rgba(255,255,255,0.65);
}


/* Dark HUD */
.body--dark .location-card-hud {
    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.10) 0%,
            transparent 30%
        );

    border-color: rgba(255,255,255,0.18);
}


/* =========================================================
   Content
   ========================================================= */

.location-card-content {
    position: relative;

    z-index: 3;

    width: 100%;
    min-height: 260px;

    padding: 24px;
}


/* =========================================================
   Eyebrow
   ========================================================= */

.location-eyebrow {
    font-size: 9px;
    font-weight: 600;

    letter-spacing: 0.28em;

    color: rgba(50, 65, 78, 0.48);

    margin-bottom: 3px;

    transition: color 0.25s ease;
}


.body--dark .location-eyebrow {
    color: rgba(220, 230, 238, 0.48);
}


/* =========================================================
   Title
   ========================================================= */

.location-title {
    font-size: 27px;
    line-height: 1.15;

    font-weight: 700;

    letter-spacing: 0.01em;

    color: #1b2735;

    text-shadow:
        0 1px 1px rgba(255,255,255,0.8);

    transition:
        color 0.25s ease,
        text-shadow 0.25s ease;
}


.body--dark .location-title {
    color: #edf2f5;

    text-shadow:
        0 1px 3px rgba(0,0,0,0.55);
}


/* =========================================================
   Region
   ========================================================= */

.location-region {
    margin-top: 7px;

    padding-left: 10px;

    border-left: 2px solid rgba(35, 125, 130, 0.75);

    font-size: 13px;
    font-weight: 600;

    color: #26787d;

    transition: color 0.25s ease;
}


.body--dark .location-region {
    color: #61b8bc;

    border-left-color: rgba(85, 180, 185, 0.80);
}


/* =========================================================
   Coordinate
   ========================================================= */

.location-coordinate-row {
    margin-top: 24px;

    align-items: center;

    gap: 9px;
}


.location-coordinate-icon {
    font-size: 20px;

    color: rgba(70, 85, 96, 0.55);

    transition: color 0.25s ease;
}


.body--dark .location-coordinate-icon {
    color: rgba(210, 220, 228, 0.58);
}


.location-coordinate {
    font-size: 12px;

    font-weight: 500;

    letter-spacing: 0.04em;

    color: rgba(55, 68, 80, 0.72);

    font-variant-numeric: tabular-nums;

    transition: color 0.25s ease;
}


.body--dark .location-coordinate {
    color: rgba(220, 228, 234, 0.72);
}


/* =========================================================
   GPS button
   ========================================================= */

.location-gps-button {
    align-self: flex-start;

    margin-top: auto;

    min-height: 54px;

    padding: 0 22px !important;

    border: 1px solid rgba(255,255,255,0.80);

    border-radius: 10px;

    background:
        rgba(255,255,255,0.28);

    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);

    color: #263746;

    box-shadow:
        0 2px 12px rgba(0,0,0,0.06);

    transition:
        background 0.25s ease,
        border-color 0.25s ease,
        color 0.25s ease,
        box-shadow 0.25s ease;
}


/* Dark button */
.body--dark .location-gps-button {
    background:
        rgba(30, 38, 45, 0.48);

    border-color:
        rgba(255,255,255,0.22);

    color: #e7edf1;

    box-shadow:
        0 3px 14px rgba(0,0,0,0.25);
}


/* =========================================================
   Hover
   ========================================================= */

.location-gps-button:hover {
    background:
        rgba(255,255,255,0.42);
}


.body--dark .location-gps-button:hover {
    background:
        rgba(55, 65, 74, 0.58);
}

"""