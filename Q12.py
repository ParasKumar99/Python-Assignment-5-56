f = open("students.txt", "w")

names = ["Paras\n", "Nitin\n", "Rohit\n", "Palak\n", "Alok"]

f.writelines(names)

f.close()

print("Names Saved Successfully")