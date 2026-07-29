(() => {
    'use strict';

    const NAV_SELECTOR = '.floating-nav';
    const ITEM_SELECTOR = '.floating-nav-item';

    function initFloatingNav() {
        const nav = document.querySelector(NAV_SELECTOR);
        if (!nav || nav.dataset.initialized === 'true') {
            return;
        }
        nav.dataset.initialized = 'true';
        const items = Array.from(nav.querySelectorAll(ITEM_SELECTOR));
        if (!items.length) {
            return;
        }
        const count = items.length;
        let dragging = false;
        let startX = 0;
        let currentIndex = 0;
        /* Pythonから渡された初期値。DOMの内容を信用してURLを作ることはしない。*/
        const initialIndex = Number(nav.dataset.current);
        if (
            Number.isInteger(initialIndex) &&
            initialIndex >= 0 &&
            initialIndex < count
        ) {
            currentIndex = initialIndex;
        }

        function setIndex(index, animate = true) {
            index = Math.max(0, Math.min(count - 1, index));
            currentIndex = index;
            nav.style.setProperty('--nav-index', String(index));
            nav.style.setProperty('--nav-count', String(count));
            if (!animate) {
                nav.querySelector('.floating-nav-cursor')?.style.setProperty('transition', 'none');
            }
            items.forEach((item, i) => {
                item.dataset.active =
                    i === index ? 'true' : 'false';
            });
        }

        function updateFromX(clientX) {
            const rect = nav.getBoundingClientRect();
            const x = clientX - rect.left - 6;
            const usableWidth = rect.width - 12;
            const raw = x / (usableWidth / count);
            const index = Math.round(raw - 0.5);
            setIndex(index);
        }

        function navigate(index) {
            const item = items[index];
            if (!item) {
                return;
            }
            /*
            * URLはHTML側から取得しない。
            * data-indexだけをクリックイベントとして
            * NiceGUI側へ渡す。
            */
            item.click();
        }

        nav.addEventListener(
            'pointerdown',
            (event) => {
                if (event.pointerType === 'mouse' &&
                    event.button !== 0) {
                    return;
                }
                dragging = true;
                startX = event.clientX;
                nav.setPointerCapture(event.pointerId);
                nav.classList.add('is-dragging');
                updateFromX(event.clientX);
                event.preventDefault();
            },
            { passive: false }
        );

        nav.addEventListener(
            'pointermove',
            (event) => {
                if (!dragging) {
                    return;
                }
                updateFromX(event.clientX);
                event.preventDefault();
            },
            { passive: false }
        );

        nav.addEventListener(
            'pointerup',
            (event) => {
                if (!dragging) {
                    return;
                }
                dragging = false;
                nav.classList.remove('is-dragging');
                setIndex(currentIndex);
                navigate(currentIndex);
                event.preventDefault();
            },
            { passive: false }
        );

        nav.addEventListener(
            'pointercancel',
            () => {
                dragging = false;
                nav.classList.remove('is-dragging');
                setIndex(currentIndex);
            }
        );

        /*
        * 通常クリックもサポート。
        */
        items.forEach((item, index) => {
            item.addEventListener(
                'click',
                (event) => {
                    if (dragging) {
                        event.preventDefault();
                        return;
                    }
                    setIndex(index);
                }
            );
        });

        setIndex(currentIndex, false);
    }

    /*
    * NiceGUIのページ遷移やPWA復帰時にも
    * 再初期化できるようにする。
    */
    function observe() {
        initFloatingNav();

        const observer = new MutationObserver(() => {
            initFloatingNav();
        });
        observer.observe(document.body, {childList: true, subtree: true});
    }

    if (
        document.readyState === 'loading'
    ) {
        document.addEventListener('DOMContentLoaded', observe, { once: true });
    } else {
        observe();
    }
})();