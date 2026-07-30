def css_floating_nav():
    return """
    
.floating-nav {
    --nav-index: 0;
    --nav-count: 3;
    position: fixed;
    left: 50%;
    bottom: calc(14px + env(safe-area-inset-bottom));
    width: min(360px, calc(100vw - 32px));
    height: 68px;
    transform: translateX(-50%);
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    padding: 5px;
    border-radius: 999px;
    backdrop-filter: blur(28px) saturate(180%);
    -webkit-backdrop-filter: blur(28px) saturate(180%);
    background: var(--color-nav-bg-light);
    border: 1px solid rgba(25, 25, 25, .16);
    box-shadow:
        0 8px 30px rgba(0, 0, 0, .12),
        inset 0 1px 0 rgba(255, 255, 255, .55);
    z-index: 9999;
    touch-action: none;
    user-select: none;
    -webkit-user-select: none;
    -webkit-tap-highlight-color: transparent;
    isolation: isolate;
}


/* 選択カーソル */
.floating-nav-cursor {
    position: absolute;
    top: 5px;
    left: 5px;
    width: calc((100% - 10px) / var(--nav-count));
    height: calc(100% - 10px);
    border-radius: 999px;
    background: rgba(255, 255, 255, .42);
    border: 1px solid rgba(25, 25, 25, .16);
    box-shadow:
        inset 0 1px 0 rgba(255, 255, 255, .55),
        0 2px 8px rgba(0, 0, 0, .08);
    transform: translateX(calc(var(--nav-index) * 100%));
    transition: transform .28s cubic-bezier(.2, .8, .2, 1);
    pointer-events: none;
    z-index: 0;
}


/* Dark Mode */
.body--dark .floating-nav {
    background: var(--color-nav-bg-dark);
    border: 1px solid rgba(255, 255, 255, .16);
}

.body--dark .floating-nav-cursor {
    background: rgba(255, 255, 255, .12);
    border: 1px solid rgba(255, 255, 255, .16);
    box-shadow:
        inset 0 1px 0 rgba(255, 255, 255, .18),
        0 2px 8px rgba(0, 0, 0, .18);
}


/* 各項目 */
.floating-nav-item {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 3px;
    border-radius: 19px;
    cursor: pointer;
    z-index: 1;
    transition: transform .15s ease;
    -webkit-tap-highlight-color: transparent;
}

/* アイコン */
.floating-nav-icon {
    font-size: 21px;
    line-height: 1;
    opacity: .75;
    transition:
        transform .2s ease,
        opacity .2s ease;
}

/* 文字 */
.floating-nav-label {
    font-size: 10px;
    line-height: 1.1;
    font-weight: 500;
    white-space: nowrap;
    opacity: .70;
    transition:
        opacity .2s ease,
        font-weight .2s ease;
}

/* アクティブ */
.floating-nav-item.is-active .floating-nav-icon {
    opacity: 1;
    transform: scale(1.04);
}

.floating-nav-item.is-active .floating-nav-label {
    opacity: 1;
    font-weight: 600;
}

/* 押したとき */
.floating-nav-item:active {
    transform: scale(.94);
}

"""