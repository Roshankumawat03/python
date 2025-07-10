# Character Case Checker
# Take a single character from the user and check if it's an uppercase letter, a lowercase letter, or not a letter at all.

# uppercase letter = A 
# lowercase letter = a

character = input("Enter a single character: ")

if character.isupper():
    print("character is an uppercase letter.")
elif character.islower():
    print("character is a lowercase letter.")
else:
     print("character is not a letter.")