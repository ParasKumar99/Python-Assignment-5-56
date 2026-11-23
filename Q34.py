f = open("sample.txt", "r")

data = f.read()

words = data.replace(",", "").split()

count = words.count("Hare")

print("Hare Occurrences:", count)

f.close()