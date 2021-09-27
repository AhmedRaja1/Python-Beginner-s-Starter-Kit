from pathlib import Path
path = Path(r"C:\Users\RELIANCE\Desktop\MCT Cert.txt")
writing = path.write_text(data="MOsh is Great!")
read = path.read_text()
print(read)
