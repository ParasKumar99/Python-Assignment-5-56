import os

filename = "sample.txt"

if os.path.exists(filename):
    print("File Exists")
    print("File Size:", os.path.getsize(filename), "bytes")
else:
    print("File Not Found")