import os

f = open("test.txt", "w")

f.write("Hare Krishna, Hare Rama")

f.close()

f = open("test.txt", "r")

print("Content:", f.read())

f.close()

print("File Closed:", f.closed)

os.remove("test.txt")

print("File Deleted Successfully")