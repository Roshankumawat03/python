# Write a Python program to swap two variables.

# Output Should Look Like this:
# Enter the value of the first variable (a): 5
# Enter the value of the second variable (b): 9
# Original values: a = 5, b = 9
# Swapped values: a = 9, b = 5

a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the second variable (b): ")

print(f"Original values: a = {a}, b = {b}")

a, b = b, a

print(f"Swapped values: a = {a}, b = {b}")