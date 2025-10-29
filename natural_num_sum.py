# Write a Python Program to Find the Sum of Natural Numbers.
# Natural numbers are a set of positive integers that are used to count and order objects.
# They are the numbers that typically start from 1 and continue indefinitely, including all the
# whole numbers greater than 0. In mathematical notation, the set of natural numbers is often
# denoted as "N" and can be expressed as:
# 𝑁 = 1,2,3,4,5,6,7,8,...

# Output Should Look Like this:
# Enter the limit: 10
# The sum of natural numbers up to 10 is: 55

n = int(input("Enter the limit: "))

sum = 0

for i in range(1, n + 1):
    sum += i

print(f"The sum of natural numbers up to {n} is: {sum}")

