f = open("sample.txt", "r")

for line in f:
    if "Rama" in line:
        print(line, end="")

f.close()