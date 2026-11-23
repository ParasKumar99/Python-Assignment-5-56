f = open("sample.txt", "r")

for line in f:
    if line.startswith("H"):
        print(line, end="")

f.close()