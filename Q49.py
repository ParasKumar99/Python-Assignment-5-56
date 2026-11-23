import os

f = open("old.txt", "w")

f.write("Hare Krishna, Hare Rama")

f.close()

os.rename("old.txt", "new.txt")

f = open("new.txt", "r")

print(f.read())

f.close()