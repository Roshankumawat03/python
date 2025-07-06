# Age Category Checker
# Take the user's age as input and print a message indicating if they are a child, teenager, adult, or senior.
 
# Child = 10
# Teenager = 18
# Adult = 35
# Senior = 35>

age = int(input("Enter Your Age: "))

if age <= 10:
 print("Person is a Child.")
elif age > 10 and age <= 18:
 print("Person is a Teenager.")
elif age > 18 and age <= 35:
 print("Person is a Adult.")
else:
  print("Person is a Senior.") 