f = open("lines.txt", "w")

lines = [
    "Hare Krishna\n",
    "Hare Rama\n",
    "Radhe Radhe\n"
]

f.writelines(lines)

f.close()

print("Lines Written Successfully")