f1 = open("sample.txt", "r")

data1 = f1.read()

f1.close()

f2 = open("welcome.txt", "w")

f2.write("Radhe Radhe")

f2.close()

f2 = open("welcome.txt", "r")

data2 = f2.read()

f2.close()

f3 = open("merged.txt", "w")

f3.write(data1 + "\n" + data2)

f3.close()

print("Files Merged Successfully")