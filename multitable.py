# 7. Write a Python Program to Display the multiplication Table.


# Output Should Look Like this:
# Display multiplication table of: 19
# 19 X 1 = 19
# 19 X 2 = 38
# 19 X 3 = 57
# 19 X 4 = 76
# 19 X 5 = 95
# 19 X 6 = 114
# 19 X 7 = 133
# 19 X 8 = 152
# 19 X 9 = 171
# 19 X 10 = 190

num = int(input("Display multiplication table of: "))

for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")