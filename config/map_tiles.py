MAP_TILES = {
    "standard": {
        "url": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        "options": {
            "maxZoom": 19,
            "attribution": "&copy; OpenStreetMap contributors",
        },
    },
    "satellite": {
        "url": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        "options": {
            "maxZoom": 19,
            "attribution": "Tiles &copy; Esri",
        },
    },
    "terrain": {
        "url": "https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png",
        "options": {
            "maxZoom": 17,
            "attribution": (
                "&copy; OpenStreetMap contributors, "
                "&copy; OpenTopoMap"
            ),
        },
    },
}