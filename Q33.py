f = open("sample.txt", "r")

data = f.read()

digits = 0
special = 0

for ch in data:
    if ch.isdigit():
        digits += 1
    elif not ch.isalnum() and not ch.isspace():
        special += 1

print("Digits:", digits)
print("Special Characters:", special)

f.close()