f = open("sample.txt", "r")

data = f.read()

f.close()

f = open("upper.txt", "w")

f.write(data.upper())

f.close()

print("File Converted Successfully")