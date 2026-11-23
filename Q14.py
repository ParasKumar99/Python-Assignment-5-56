text = input("Enter Text: ")

f = open("user.txt", "w")

f.write(text)

f.close()

print("Data Saved Successfully")