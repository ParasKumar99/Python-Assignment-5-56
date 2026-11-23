f = open("sample.txt", "r")

print("Position:", f.tell())

f.read(5)

print("New Position:", f.tell())

f.close()