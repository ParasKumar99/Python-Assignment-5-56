name = input("Enter Name: ")
roll = input("Enter Roll Number: ")
marks = input("Enter Marks: ")

f = open("student.txt", "w")

f.write("Name: " + name + "\n")
f.write("Roll Number: " + roll + "\n")
f.write("Marks: " + marks)

f.close()

print("Student Details Saved")