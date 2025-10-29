# Write a Python Program to Check Prime Number.
# A prime number is a whole number that cannot be evenly divided by any other number
# except for 1 and itself. For example, 2, 3, 5, 7, 11, and 13 are prime numbers because they
# cannot be divided by any other positive integer except for 1 and their own value.

# Output Should Look Like this:
# Enter a number: 27
# 27, is not a prime number

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num}, is not a prime number")
            break
    else:
        print(f"{num}, is a prime number")
else:
    print(f"{num}, is not a prime number")