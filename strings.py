# A string in Python is a sequence of characters enclosed in quotes. You can define a string using either single quotes 
# (' ') or double quotes (" "), or even triple quotes (''' ''' or """ """) for multi-line strings.


# Creating Strings:

#     Single Quote: 'hello'

#     Double Quote: "hello"

#     Triple Quote: '''hello''' or """hello""" (used for multi-line strings)


# String Operations:

# Concatenation: You can combine two or more strings using the + operator.

# str1 = "Hello"
# str2 = 'World'
# result = str1 + str2
# print(result)  # Output: HelloWorld

# Repetition: You can repeat a string multiple times using the * operator.

# str1 = "Hello"
# result = str1 * 3
# print(result)  # Output: HelloHelloHello


# Indexing: Each character in a string has an index. The index starts at 0 for the first character.
# To access these values we use `[]` operator.

# my_string = "Hello"
# print(my_string[0])  # Output: H
# print(my_string[-1])  # Output: o (Negative index starts from the end)
# print(my_string[50]) #IndexError: string index out of range


# Slicing: You can extract a substring by using slicing notation [start:end].
# For slicing we use `:` operator in side `[]`
# if we enter wrong index it won't give any error but can lead to blank output 

# my_string = "Hello"
# [from:to:in_what_order]
# where_to cuts by -1

# print( my_string[ 1: ] ) # ello

# print(my_string[ 1:4 ])  # Output: ell (Extracts from index 1 to 3)
# print(my_string[ :3 ])   # Output: Hel (Extracts from index 0 to 2)

# my_string = "0123456789"

# print(my_string[ 1:10:3 ])   # Output: 147
# print(my_string[ -8:-1 ])   # Output: 23456789
# print(my_string[ -8::-1 ])   # Output: 210
# print(my_string[ -5:1:-1 ])   # Output: 5432

# my_string = "abcdefghijklmn"
# print(my_string[ ::-1 ])   # Output: nmlkjihgfedcba
# print(my_string[ ::-3 ])   # Output: nkheb
# print(my_string[ ::-2 ])   # Output: nljhfdb


# Length: You can get the length of a string using the len() function.

# my_string = "Jaipur"
# print( len(my_string) )  # Output: 6

# Membership: Check if a substring exists in a string using in or not in.

# my_string = "Hello World"
# # print("Hello" in my_string)  # Output: True
# print("h" in my_string)  # Output: False

# String Manipulation / Strings are Immutable
# a = "Hello"
# a = "W" + a[1:]
# print( a ) # Wello

# String Methods: Python strings have a variety of built-in methods. Some of the commonly used methods are:
# We use `.` operator to call a method
# upper(): Converts the string to uppercase.

# my_string = "hello123"
# new_string =  my_string.upper()
# print( new_string )  # Output: HELLO123
# print(my_string) # hello123

# lower(): Converts the string to lowercase.

# my_string = "HELLO"
# print(my_string.lower())  # Output: hello

# strip(): Removes leading and trailing whitespaces.

# my_string = "  hello  "
# print(my_string.strip())  # Output: hello

# my_string = "--hel-lo--"
# print(my_string.strip("-"))  # Output: hel-lo

# my_string = "  hello  "
# print(my_string.lstrip())  # Output: hello

# my_string = "  hello  "
# print(my_string.rstrip())  # Output: hello

# replace(old, new): Replaces occurrences of a substring.

# my_string = "Hello World"
# print(my_string.replace("World", "Python"))  # Output: Hello Python

# my_string = "Hello World"
# print(my_string.replace("o", "-"))  #Output: Hell- W-rld

# split(): Splits the string into a list based on a delimiter (default is whitespace).

# my_string = "my name is vipin"
# print(my_string.split())  # Output: ['my', 'name', 'is', 'vipin']

# my_string = "15/7/2025"
# print(my_string.split("/"))  # Output: ['15', '7', '2025']

# join(iterable): Joins elements of an iterable (like a list) into a single string, with a specified separator.

# words = ['my', 'name', 'is', 'vipin']
# print("".join(words))  # Output: mynameisvipin
# print(" ".join(words))  # Output: my name is vipin

# words = ['15', '7', '2025']
# print( "-".join(words) )

# find(substring): Returns the index of the first occurrence of a substring (or -1 if not found).

# my_string = "Hello World"
# print(my_string.find("o"))  # Output: 4

# count(substring): Counts occurrences of a substring in the string.

# my_string = "Hello World, Hello Python"
# print(my_string.count("Hello"))  # Output: 2

# username = "lyfofvipin"
# my_string = input("Enter Your Username: ")
# if username.casefold() == my_string.casefold():
#     print("Correct Name")
# else:
#     print("Incorrect Name")

# a = "23sdfsafd"
# print( a.isalnum() )
# int(a)
# if a.isnumeric():
#     int(a)
# else:
#     print("String is not numeric")

# a = "my name is vipin"
# print(a.capitalize())
# print(a.title())

a = "my name is vipin"
counter = 0

while counter < len(a):
    if counter == 0:
        print(a[0].upper())
    else:
        print(a[counter])
    counter += 1
