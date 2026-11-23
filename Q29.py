f = open("sample.txt", "r")

f.seek(13)

print(f.read())

f.close()