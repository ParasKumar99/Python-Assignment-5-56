import os

if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")
    print("Directory Created Successfully")
else:
    print("Directory Already Exists")