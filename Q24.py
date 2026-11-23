f = open("sample.txt", "r+")

print("Old Data:")
print(f.read())

f.seek(0)

f.write("Radhe")

f.seek(0)

print("New Data:")
print(f.read())

f.close()