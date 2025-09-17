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


# total = 0

# while True:
#     number = int(input("Enter A Number: "))
#     if number == 0:    
#         print("0 is not added")
#         continue
#     print("Doing calculations")
#     if number < 0:
#         exit(1)
#     else:
#         total = total + number
# print(f"Sum of all values are {total}")

# Just like break we have another statement, continue, which skips the execution of the code after itself and goes back to the start of the loop.
# That means it will help you to skip a part of the loop.
# In the below example we will ask the user to input an integer, if the input is negative then we will ask again, if positive then we will square the number.
# To get out of the infinite loop user must input 0.

while True:

    num = int(input("Enter an integer: "))

    if num == 0:
        print("Exiting the loop.")
        break

    if num < 0:
        print("Negative number, try again.")
        continue

    square = num * num
    print(f"the square of {num} is {square}")