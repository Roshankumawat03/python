# Write a function to display Days in a Month
# Ask the user to input a month (1–12) and print how many days are in that month (consider leap year for February).
# def days_in_month():
#     month = int(input("Enter month (1-12): "))
#     year = int(input("Enter year: "))
#     if month in [1, 3, 5, 7, 8, 10, 12]:
#         print("31 days")
#     elif month in [4, 6, 9, 11]:
#         print("30 days")
#     elif month == 2:
    
#         if (year % 4 == 0):
#             print("29 days (Leap Year)")
#         else:
#             print("28 days")
#     else:
#         print("Invalid month")

# days_in_month()        


# Write a function to display  Leap Year Checker
# Ask the user to input a year and determine whether it is a leap year or not.

# def leap_year_checker():
#     year = int(input("Enter A Year: "))
#     if(year % 4 == 0):
#         print("It's a leap year") 
#     else:
#         print("It's not a leap year") 

# leap_year_checker()      


# Write a function to display Evenly Divisible
# Ask the user for a number and check if it's divisible by both 4 and 6.

# def evenly_divisible():
#     num = int(input("Enter a number: "))
#     if(num % 4 == 0 and num % 6 == 0):
#         print("num is divisible by both 4 and 6")
#     else:
#         print("num is not divisible by both 4 and 6")
# evenly_divisible()            

# Write a function to display Character Case Checker
# Take a single character from the user and check if it's an uppercase letter, a lowercase letter, or not a letter at all.

# def character_case_checker():
#     char = input("Enter a single character: ")
#     if len(char) != 1:
#         print("Please enter only one character.")
#     elif 'A' <= char <= 'Z':
#         print("Uppercase letter")
#     elif 'a' <= char <= 'z':
#         print("Lowercase letter")
#     else:
#         print("Not a letter")

# character_case_checker()        

# Write a function to display Time of Day Greeting
# Ask the user to enter the time (in hours) and print a greeting based on the time of day:
#     Morning (5 AM - 12 PM)
#     Afternoon (12 PM - 5 PM)
#     Evening (5 PM - 9 PM)
#     Night (9 PM - 5 AM)

# hour = 0-23
# def time_of_day_greeting():
#     hour = int(input("Enter the hour: "))
#     if 5 <= hour < 12:
#         print("good morning")
#     elif 12 <= hour < 17:
#         print("good afternoon")   
#     elif 17 <= hour < 21:
#         print("good evening")
#     else:
#         print("good night")  

# time_of_day_greeting()


# Write a function to display the sum of the first 10 natural numbers.

# def sum_of_the_first_10():
#     total = sum(range(1,11))
#     print("Sum of first 10 natural numbers:", total)
# sum_of_the_first_10() 

# def sum_of_the_first_10():
#     add = 0
#     for x in range(1, 11):
#         add = add + x
#     print(add)
# sum_of_the_first_10()       

# Write a function to display print even numbers from 2 to 10.

# def print_even_number():
#  for x in range(2, 11, 2):
#     print(x)
# print_even_number()

# Write a function to display calculate the factorial of a given number.

# def factorial():
#     num = int(input("Enter a number: "))
#     fact = 1
#     for i in range(1, num + 1):
#         fact *= i
#     print(f"Factorial of {num} is {fact}")

# factorial()    


# Write a function to display print numbers in a countdown from 10 to 1.

# def countdown():
#     for x in range(10, 0, -1):
#         print(x)
# countdown()        

# Write a function to display Sum of Even Numbers: 
# Write a program that asks the user to enter a positive integer N. Use a while loop to iterate from 1 up to N. Inside the loop, use an if statement to check if the current number is even. If it is, add it to a running total. Finally, print the sum of all even numbers up to N.


# def sum_of_even_number( number ):
#     sum = 0
#     for x in range(2, number + 1):
#         if x % 2 == 0:
#             sum += x
#     return sum


# number = int(input("Enter A Number: "))
# result = sum_of_even_number(number) 
# print(result)       


# def sum_of_even_numbers():
#     num = int(input("Enter a positive integer: "))
#     total = 0
#     i = 1
#     while i <= num:
#         if i % 2 == 0:
#             total += i
#         i += 1
#     print("Sum of even numbers up to", num, "is:", total)
# sum_of_even_numbers()    

# Write a function to display to find and print the smallest divisor of that number (excluding 1). Use an if-else statement to handle the case where the number itself is prime (its smallest divisor will be itself).
# def smallest_divisor():
#     n = int(input("Enter a number: "))
#     if n <= 1:
#         print("Enter a number greater than 1")
#         return
#     for x in range(2, n + 1):
#         if n % x == 0:
#             print(f"Smallest divisor of {n} is {x}")
#             break
# smallest_divisor()        



# def smallest_divisor(number):
#     for x in range(2, number):
#         if number % x == 0:
#             print(x)
#             break
#     if x == number -1:
#         print("Not divided by anyone") 

# smallest_divisor(25)