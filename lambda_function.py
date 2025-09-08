# Lambda Functions

# A lambda function (also called an anonymous function) is a small, 
# single-expression function that doesn't have a name. 
# You create them when you need a simple function for a short period, 
# typically as an argument to a higher-order function like map(), filter(), or sorted().

# The Syntax
# The syntax is simple and concise: lambda arguments: expression
#     lambda: The keyword used to create a lambda function.
#     arguments: The input arguments, just like in a regular function.
#     expression: A single expression that is evaluated and returned.

# A regular function to add two numbers
def add(a, b):
    return a + b

# lambda a, b: a+b
# add = lambda a, b: a + b

print( add( 2, 3 ) )