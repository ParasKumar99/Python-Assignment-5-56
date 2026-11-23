import os

f = open("old.txt", "w")
f.write("Hare Krishna")
f.close()

os.rename("old.txt", "new.txt")

print("File Renamed Successfully")