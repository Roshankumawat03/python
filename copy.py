# copy.py

# Enter source file you want to copy: C:\Users\JITENDRA KUMAWAT\OneDrive\Desktop\python\folder2\dummy.txt
# Enter destination file where you want to copy: hw.txt

# SC1 -> src file does not exist
# -> Please re run and enter a valid file name

# SC2 -> destination file is already there
# -> Do you want to replace the file content?: yes


import os

source = input("Enter source file you want to copy: ")

if os.path.exists(source):
    destination = input("Enter destination file you want to copy: ")
    
    if os.path.exists(destination):
        file_clean_validation = input("Do you want to replace the existing file ? Yes/No : ")

        if file_clean_validation == "yes":    
            with open(source) as file_to_copy:
                data = file_to_copy.readlines()

            with open(destination, "w") as file_to_paste:
                file_to_paste.writelines(data)
    else:
        with open(source) as file_to_copy:
                data = file_to_copy.readlines()

        with open(destination, "w") as file_to_paste:
            file_to_paste.writelines(data)

else:
    print("File does not exist")        