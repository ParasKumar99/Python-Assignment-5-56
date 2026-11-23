import os

filename = "sample.txt"

if os.path.exists(filename):
    print("File Exists")
else:
    print("File Not Found")