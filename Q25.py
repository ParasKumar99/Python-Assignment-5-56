f = open("demo.txt", "w+")

f.write("Hare Krishna")

f.seek(0)

print(f.read())

f.close()