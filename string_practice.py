# Palindrome Checker:
# Write a program that repeatedly asks the user to enter a word. 
# Use a while loop to continue prompting until the user enters "exit". 
# For each word entered (before "exit"), use an if-else statement to determine if the word is a palindrome (reads the same forwards and backwards, e.g., "madam", "level"). 
# Print whether the word is a palindrome or not. (Hint: You might need string slicing or a loop to reverse the string for comparison).

# data = "amit"

# if data == data [ ::-1 ]:
#     print("It's a Palindrome")
# else:
#     print("It's not a Palindrome")  

# # Output
# data = "121"   # It's a Palindrome
# data = "122"   # It's not a Palindrome
# data = "madam" # It's a Palindrome
# data = "amit"  # It's not a Palindrome


# Sentence Word Counter:
# Ask the user to enter sentences one by one. 
# Use a while loop to keep accepting input until the user types "STOP" (case-insensitive). 
# For each sentence entered, use an if-else statement to check if the sentence contains more than 5 words. 
# Print the sentence and indicate if it's "Long sentence!" or "Short sentence!". (Hint: You can split the sentence into words using split() and then check the length of the resulting list).

# while True:

#     data = input("Enter Your Sentence: ")

#     if data.lower() == "stop":
#         break
#     if data.count(" ") +1 > 5:
#         print("It's a long Sentence.")
#     else:
#         print("It's a short Sentence.")

# Output
# Enter Your Sentence: e r t h j k
# It's a long Sentence.
# Enter Your Sentence: d f g r
# It's a short Sentence.
# Enter Your Sentence: stop


# Ask the user to type a string. Use a while loop to process characters one by one (you can iterate using an index that increments). Maintain counts for:

# Uppercase letters
# Lowercase letters
# Digits

# Special characters (anything else)
# Use if-elif-else statements to categorize each character. 
# Stop the loop if you encounter the character '#'. Finally, print the counts for each type of character.

# count_upper = count_lower = count_digit = count_spl = 0

# data = "abcd126789788gfjfjmJLK#$^^^^*))(@HN34ABCD()[]"
# length = len(data)

# counter = 0

# while counter < length:

#     if data[counter] in "abcdefghijklmnopqrstuvwxyz":
#         count_lower += 1
#     elif data[counter] in "1234567890": # "1" .isnumeric()
#         count_digit += 1
#     elif data[counter] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         count_upper += 1
#     else:
#         count_spl += 1    
#     counter += 1    

# print(f"Count of Lower are {count_lower}, Count of Upper are {count_upper}, Count of Digit are {count_digit}, Count of SPL Char are {count_spl} ")

# Output
# Count of Lower are 10, Count of Upper are 9, Count of Digit are 11, Count of SPL Char are 15