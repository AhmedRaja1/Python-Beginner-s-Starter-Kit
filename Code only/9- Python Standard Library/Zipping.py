from pathlib import Path
from zipfile import ZipFile
with ZipFile(r"C:\Users\RELIANCE\Desktop\free.zip") as zip:
    zip.extractall(r"C:\Users\RELIANCE\Desktop\khulna")
