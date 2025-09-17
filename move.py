# move.py

# Enter source file you want to copy: C:\Users\JITENDRA KUMAWAT\OneDrive\Desktop\python\folder2\dummy.txt
# Enter destination file where you want to copy: hw.txt

# SC1 -> src file does not exist
# -> Please re run and enter a valid file name

# SC2 -> destination file is already there
# -> Do you want to replace the file content?: yes

# SC3 -> delete the src file


import os

source = input("Enter source file you want to move: ")
destination = input("Enter destination file you want to copy: ")
    
with open(source) as file_to_move:
    data = file_to_move.readlines()

with open(destination, "w") as file_to_paste:
    file_to_paste.writelines(data)

os.remove(source)
       