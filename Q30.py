f = open("sample.txt", "r")

print("Before Closing:", f.closed)

f.close()

print("After Closing:", f.closed)