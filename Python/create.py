import os

if "system.txt" not in os.listdir():
    file = open ('system.txt',"x")
    print("file create")
else:
    print("file already exists")