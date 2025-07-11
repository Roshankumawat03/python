# counter = 1

# while counter <= 5:
#   counter += 1
#   print(counter) 

 # print(f"Final Counter Value is {counter}") 

# Write a while loop to count from 1 to 5.

# counter = 1

# while counter <= 5:
#  print(counter)
#  counter += 1


#  Write a while loop to print even numbers from 2 to 10.
# num = 2

# while num <= 10:
#     print(num)
#     num += 2

# Write a while loop to print numbers in a countdown from 10 to 1.
# num = 10

# while num >= 1:
#     print(num)
#     num -= 1

# Write a while loop to find the sum of the first 10 natural numbers.
# counter = 1
# sum = 0
# while counter <= 10:
#     sum = sum + counter 
#     print(f"number is{counter}")
#     print(f"new sum is {sum}")
#     counter += 1
# print(sum)

# Write a while loop to calculate the factorial of a given number.    
# counter = 1
# mul = 1
# while counter <= 10:
#     mul = mul * counter 
#     print(f"number is {counter}")
#     print(f"new mul is {mul}")
#     counter += 1
# print(mul)

# Sum of Even Numbers: Write a program that asks the user to enter a positive integer N. Use a while loop to iterate from 1 up to N. Inside the loop, use an if statement to check if the current number is even. If it is, add it to a running total. Finally, print the sum of all even numbers up to N.

# counter = 2
# sum = 0

# while counter <= 10:
#     sum = sum + counter 
#     print(counter,sum)
#     counter +=2
# print(sum)    

# counter = 1
# sum = 0

# while counter <= 10:
#     if counter % 2 == 0: 
#         sum = sum + counter
#         print(counter,sum)
#     counter +=1
# print(sum)    

# Use a while loop to keep prompting the user to enter the password until they enter it correctly. Inside the loop, use if-else statements to tell the user if their attempt was "Incorrect password. Try again." or "Password accepted!". Limit the number of attempts to 3. If the user fails 3 times, print "Account locked.".

# "123"
# counter = 1
# password = ""

# while counter <= 3 and password != "123":
#     password = input("Enter your password: ")
#     if password == "123":
#         print("Login Done")
#     else:
#         print("Incorrect password")
#     counter += 1
# if counter == 4:
#     print("Account Locked.") 
        
#Ask the user to enter an integer greater than 1. Use a while loop to find and print the smallest divisor of that number (excluding 1). Use an if-else statement to handle the case where the number itself is prime (its smallest divisor will be itself).

# counter = 2

# number = int(input("Enter A Number: "))

# # 25

# while number > 1 and number % counter != 0:
#     print(number,counter)
#     counter += 1
# if number == counter:
#     print("Failed to find the smallest divisor as it's a prime number.")
# else:
#     print(f"Number is divisible by {counter}")


#Positive Number Accumulator: Write a program that continuously asks the user to enter numbers. Use a while loop to keep taking input until the user enters a negative number. For each positive number entered, add it to a running total. Finally, print the total sum of all positive numbers entered.

# number = 0
# total = 0

# while number >= 0:

#     number = int(input("Enter A Number: "))
#     if number > 0:
#         total = total + number
# print(f"Sum of all value are {total}")  


