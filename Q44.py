import os

if os.path.exists("new.txt"):
    os.remove("new.txt")
    print("File Deleted Successfully")
else:
    print("File Not Found")