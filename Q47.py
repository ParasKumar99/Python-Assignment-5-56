import os

path = "sample.txt"

if os.path.isfile(path):
    print("It is a File")
elif os.path.isdir(path):
    print("It is a Directory")
else:
    print("Path Not Found")