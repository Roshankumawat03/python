# Write a Python Program to Print all Prime Numbers in an Interval of 1-10.


# Output Should Look Like this:
# Prime numbers between 1 and 10 are:
# 2
# 3
# 5
# 7

start = 1
end = 10

print("Prime numbers between 1 and 10 are:")

for num in range(start, end + 1):
    if num > 1: 
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)