f = open("sample.txt", "r")

f.seek(5)

print(f.read(10))

f.close()