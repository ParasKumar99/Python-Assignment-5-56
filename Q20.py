f = open("numbers.txt", "w")

for i in range(1, 101):
    f.write(str(i) + "\n")

f.close()

print("Numbers Saved Successfully")