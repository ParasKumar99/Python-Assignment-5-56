import os

filename = "sample.txt"

if os.path.exists(filename):
    print("File Name:", filename)
    print("File Size:", os.path.getsize(filename), "bytes")
    print("Is File:", os.path.isfile(filename))
else:
    print("File Not Found")