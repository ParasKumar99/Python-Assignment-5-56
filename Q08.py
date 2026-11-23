f = open("sample.txt", "r")
data = f.read()

print("Total Words:", len(data.split()))
f.close()