 #Evenly Divisible

 # Ask the user for a number and check if it's divisible by both 4 and 6.

num = int(input("Enter a Number: "))

if num % 4 == 0 and num % 6 == 0:
    print(f"{num} is divisible by both num.")
else:
    print(f"{num} is not divisible by both num.")    