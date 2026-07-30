def css_loading_panel():
    return """
    
.loading-card {
    width: 300px;
    padding: 28px 26px;
    background: rgba(238, 239, 241, 0.78);
    backdrop-filter: blur(40px) saturate(150%);
    -webkit-backdrop-filter: blur(40px) saturate(150%);
    border-radius: 28px;
    border: 1px solid rgba(70, 72, 76, 0.18);
    box-shadow:
        0 20px 60px rgba(0,0,0,0.12),
        0 4px 16px rgba(0,0,0,0.05),
        inset 0 1px 0 rgba(255,255,255,0.72);
    overflow: hidden;
    isolation: isolate;
}

.loading-spinner {
    margin-bottom: 14px;
}

.loading-message {
    width: 100%;
    margin-top: 0;
    font-size: 13px;
    line-height: 1.5;
    color: rgba(40,42,45,0.52);
    text-align: center;
    letter-spacing: -0.005em;
}

/* Dark Mode */
.body--dark .loading-card {
    background: rgba(30,31,34,0.76);
    border: 1px solid rgba(255,255,255,0.14);
    box-shadow:
        0 20px 60px rgba(0,0,0,0.32),
        0 4px 16px rgba(0,0,0,0.18),
        inset 0 1px 0 rgba(255,255,255,0.10);
}

.body--dark .loading-message {
    color: rgba(255,255,255,0.52);
}
    
"""
