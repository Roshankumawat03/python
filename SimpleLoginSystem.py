# Simple Login System
# Simulate a login system where the user enters a username and password. Print a success message if both are correct, otherwise print an error.

username = "admin"
password = "123"

user = input("Enter Your Username: ")
passw = input("Enter Your password: ")

if user ==username and passw == password:
 print("Login Success.")
else:
 print("Invalid Username or Password.")