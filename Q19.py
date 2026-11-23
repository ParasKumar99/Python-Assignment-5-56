n = int(input("Enter Number: "))

f = open("table.txt", "w")

for i in range(1, 11):
    f.write(f"{n} x {i} = {n*i}\n")

f.close()

print("Table Saved Successfully")