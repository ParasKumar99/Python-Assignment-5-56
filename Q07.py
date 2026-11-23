f = open("sample.txt", "r")
lines = f.readlines()

print("Total Lines:", len(lines))
f.close()