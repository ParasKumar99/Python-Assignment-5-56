f = open("sample.txt", "r")

words = f.read().replace(",", "").split()

longest = max(words, key=len)

print("Longest Word:", longest)

f.close()