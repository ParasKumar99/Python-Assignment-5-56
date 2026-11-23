f = open("demo.txt", "w")
f.write("Hare Krishna")
f.close()

f = open("demo.txt", "a")
f.write("\nHare Rama")
f.close()

f = open("demo.txt", "r")

print(f.read())

f.close()