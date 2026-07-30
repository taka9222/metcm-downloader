def js_service_worker():
    return """

if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("/static/sw.js");
}

    """