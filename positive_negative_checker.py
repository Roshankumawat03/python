# Write a Python Program to Check if a Number is Positive, Negative or Zero.

# Output Should Look Like this:
# Enter a number: 6.4
# Positive number

num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")