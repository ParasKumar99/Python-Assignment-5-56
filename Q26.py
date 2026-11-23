f = open("demo.txt", "a+")

f.write("\nHare Rama")

f.seek(0)

print(f.read())

f.close()