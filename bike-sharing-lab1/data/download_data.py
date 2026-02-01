import os
import zipfile
import urllib.request

URL = "https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip"

BASE_DIR = os.path.dirname(__file__)
OUT_DIR = os.path.join(BASE_DIR, "raw")
ZIP_PATH = os.path.join(OUT_DIR, "bike_sharing.zip")

os.makedirs(OUT_DIR, exist_ok=True)

print("Downloading:", URL)
urllib.request.urlretrieve(URL, ZIP_PATH)

print("Unzipping:", ZIP_PATH)
with zipfile.ZipFile(ZIP_PATH, "r") as z:
    z.extractall(OUT_DIR)

print("Done. Files in", OUT_DIR)
print(os.listdir(OUT_DIR))
