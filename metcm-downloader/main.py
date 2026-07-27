from nicegui import ui
import sys
import os
from urllib.request import build_opener
# import pygrib


def downloader():
    opener = build_opener()
    file = 'https://osdf-director.osg-htc.org/ncar/gdex/d083002/grib2/2026/2026.07/fnl_20260727_00_00.grib2'
    ofile = os.path.basename(file)
    sys.stdout.write("downloading " + ofile + " ... ")
    sys.stdout.flush()
    infile = opener.open(file)
    outfile = open(ofile, "wb")
    outfile.write(infile.read())
    outfile.close()
    sys.stdout.write("done\n")


def grib_loader():
    pass
    # grbs = pygrib.open("2026.07/fnl_20260727_00_00.grib2")
    # grbs.read()


def root():
    ui.sub_pages({
        '/': table_page,
        '/map/{lat}/{lon}': map_page,
    }).classes('w-full')


def table_page():
    ui.table(rows=[
        {'名称': '矢臼別演習場', '緯度': 43.2997, '経度': 144.9873},
        {'名称': '東富士演習場', '緯度': 35.2947, '経度': 138.8536},
    ]).props('flat bordered') \
        .on('row-click', downloader)


# lambda e: ui.navigate.to(f'/map/{e.args[1]["緯度"]}/{e.args[1]["経度"]}')

def map_page(lat: float, lon: float):
    ui.leaflet(center=(lat, lon), zoom=10)
    ui.link('Back to table', '/')


ui.run(root)
