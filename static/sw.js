const CACHE_NAME = 'metcm-static-v1';

const CACHE_FILES = [
    '/static/manifest.json',
    // アイコンなど、更新頻度の低いものだけ
    '/static/icons/icon-192.png',
    '/static/icons/icon-512.png',
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => cache.addAll(CACHE_FILES))
            .then(() => self.skipWaiting())
    );
});


self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(keys =>
            Promise.all(
                keys
                    .filter(key => key !== CACHE_NAME)
                    .map(key => caches.delete(key))
            )
        ).then(() => self.clients.claim())
    );
});


self.addEventListener('fetch', event => {
    const request = event.request;

    // GET以外はService Workerで処理しない
    if (request.method !== 'GET') {
        return;
    }

    const url = new URL(request.url);

    // CSS / JS / HTML はキャッシュしない
    // 常に最新版をネットワークから取得
    if (
        url.pathname.endsWith('.css') ||
        url.pathname.endsWith('.js') ||
        url.pathname.endsWith('.html')
    ) {
        event.respondWith(
            fetch(request)
        );
        return;
    }

    // その他の静的ファイルはキャッシュ優先
    event.respondWith(
        caches.match(request).then(cached => {
            return cached || fetch(request);
        })
    );
});