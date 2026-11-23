f = open("sample.txt", "r")

data = f.read()

f.close()

f = open("reverse.txt", "w")

f.write(data[::-1])

f.close()

print("Reversed Content Saved")