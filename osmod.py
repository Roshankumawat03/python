# Write a program that list all files on a folder and print files starting with `I` or `i`.

import os

# files = os.listdir()

# for x in files:
#     if x.startswith("i"):
        # print(x)

# Task:
# Chota Sa Terminal:
    # * if user type ls it will list all the files of the dir
    # * if user type lsfolder it will list all the folders only
    # * if user type lsfiles it will list all the files only

while True:
    command  = input("-->")
    if command == "ls":
        print(os.listdir())
    elif command == "lsfolder":
        data = os.listdir()
        for x in data:
            if os.path.isdir(x):
                print(x)
    elif command == "lsfiles":
        data = os.listdir()
        for x in data:
            if not os.path.isdir(x):
                print(x)
    elif command == "stop":
        break
    else:
        print("invalid command")