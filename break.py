# break
# continue
# exit

# number = 0

# while number >= 0:
#     number = int(input("Enter A Number: "))

# while True:
 
#     number = int(input("Enter A Number: "))
#     if number < 0:
#         break
   
# total = 0

# while True:
#     number = int(input("Enter A Number: "))
#     if number == 0:    
#         print("0 is not added")
#         continue
#     print("Doing calculations")
#     if number < 0:
#         break
#     else:
#         total = total + number
# print(f"Sum of all values are {total}")   


total = 0

while True:
    number = int(input("Enter A Number: "))
    if number == 0:    
        print("0 is not added")
        continue
    print("Doing calculations")
    if number < 0:
        exit(1)
    else:
        total = total + number
print(f"Sum of all values are {total}")
