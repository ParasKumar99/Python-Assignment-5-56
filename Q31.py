f = open("sample.txt", "r")

data = f.read().lower()

count = 0

for ch in data:
    if ch in "aeiou":
        count += 1

print("Total Vowels:", count)

f.close()