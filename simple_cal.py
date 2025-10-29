# Write a Python Program to Make a Simple Calculator with 4 basic mathematical
# operations.

# Output Should Look Like this:
# Select operation.
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# Enter choice(1/2/3/4): 1
# Enter first number: 5
# Enter second number: 6
# 5.0 + 6.0 = 11.0
# Let's do next calculation? (yes/no): yes
# Enter choice(1/2/3/4): 2
# Enter first number: 50
# Enter second number: 5
# 50.0 - 5.0 = 45.0
# Let's do next calculation? (yes/no): yes
# Enter choice(1/2/3/4): 3
# Enter first number: 22
# Enter second number: 2
# 22.0 * 2.0 = 44.0
# Let's do next calculation? (yes/no): yes
# Enter choice(1/2/3/4): 4
# Enter first number: 99
# Enter second number: 9
# 99.0 / 9.0 = 11.0
# Let's do next calculation? (yes/no): no

def cal():
    while True:
        print("select operation.no1.add no2.subtract no3. multiplication no4.division")
        choice = input("Enter choice(1/2/3/4):")
        number1 = float(input("Enter first number:"))
        number2 = float(input("Enter second number:")) 
        if choice == "1":
            print(f"{number1}+{number2} = {number1+number2}")
        elif choice == "2":
            print(f"{number1}-{number2} = {number1-number2}")  
        elif choice == "3":
            print(f"{number1}*{number2} = {number1*number2}")  
        elif choice == "4":
            print(f"{number1}/{number2} = {number1/number2}") 
        else:
            print("Invalid choice.")
        next_cal = input("Do next calculation?(yes/no):").lower()
        if next_cal != "yes":
            break
cal()