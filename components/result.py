from nicegui import ui

def _show_atmospheric_layers(
    layers: list[dict],
    source: dict,
    lat: float,
    lon: float,
):
    columns = [
        {
            'name': 'zone',
            'label': 'ZONE',
            'field': 'zone',
            'align': 'center',
        },
        {
            'name': 'altitude',
            'label': 'ALTITUDE [m]',
            'field': 'altitude',
            'align': 'right',
        },
        {
            'name': 'density',
            'label': 'ρ',
            'field': 'density',
            'align': 'right',
        },
        {
            'name': 'temperature',
            'label': 'T [K]',
            'field': 'temperature',
            'align': 'right',
        },
        {
            'name': 'virtual_temperature',
            'label': 'Tv [K]',
            'field': 'virtual_temperature',
            'align': 'right',
        },
        {
            'name': 'pressure',
            'label': 'P',
            'field': 'pressure',
            'align': 'right',
        },
        {
            'name': 'wind_speed',
            'label': 'WS',
            'field': 'wind_speed',
            'align': 'right',
        },
        {
            'name': 'wind_direction',
            'label': 'WD',
            'field': 'wind_direction',
            'align': 'right',
        },
        {
            'name': 'relative_humidity',
            'label': 'RH',
            'field': 'relative_humidity',
            'align': 'right',
        },
    ]

    rows = []

    for layer in layers:
        rows.append({
            'zone': f'{layer["zone"]:02d}',
            'altitude': (
                f'{layer["bottom"]:.0f}-'
                f'{layer["height"]:.0f}-'
                f'{layer["top"]:.0f}'
            ),
            'density': f'{layer["density"]:.0f}',
            'temperature': f'{layer["temperature"]:.1f}',
            'virtual_temperature': f'{layer["virtual_temperature"]:.1f}',
            'pressure': f'{layer["pressure"]:.0f}',
            'wind_speed': f'{layer["wind_speed"]:.1f}',
            'wind_direction': f'{layer["wind_direction"]:.0f}',
            'relative_humidity': f'{layer["relative_humidity"]:.3f}',
        })

    with ui.dialog() as dialog:
        with ui.card().classes('atmosphere-dialog'):

            # -------------------------------------------------
            # Header
            # -------------------------------------------------

            ui.label('ATMOSPHERIC PROFILE').classes('dialog-eyebrow')
            ui.label('大気層気象データ').classes('dialog-title')

            ui.separator().classes('dialog-separator')

            with ui.row().classes('atmosphere-meta'):
                ui.label(
                    f'LAT {lat:.4f}'
                ).classes('atmosphere-location')

                ui.label(
                    f'LON {lon:.4f}'
                ).classes('atmosphere-location')

            ui.label(
                source['time'].strftime('%Y年 %m月 %d日 %H00 UTC')
            ).classes('dialog-age')

            # -------------------------------------------------
            # Table
            # -------------------------------------------------

            ui.table(
                columns=columns,
                rows=rows,
                row_key='zone',
            ).classes('atmosphere-table')

            ui.space()

            with ui.row().classes('dialog-actions'):
                ui.button(
                    '閉じる',
                    on_click=dialog.close,
                ).props('flat').classes('dialog-cancel-button')

    dialog.open()