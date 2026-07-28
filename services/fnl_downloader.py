import os
from urllib.request import build_opener


def downloader(url):
    ofile = os.path.basename(url)
    print(f"downloading {ofile} ...")
    opener = build_opener()
    with opener.open(url) as infile:
        with open(ofile, "wb") as outfile:
            outfile.write(infile.read())
    print("done")


if __name__ == "__main__":
    downloader(input("url: "))
