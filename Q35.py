f = open("sample.txt", "r")

data = f.read()

word = "Krishna"

if word in data:
    print("Word Found")
else:
    print("Word Not Found")

f.close()