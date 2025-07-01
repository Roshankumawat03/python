# Identity Operators 

'''a=34
b=54
print(a is b)'''

'''a=[12,34,45]
b=a
#a=b=[12,34,45]
print(a is b)'''

'''a=23
b=a
#a=23
#b=23
print(a is b)'''

"""a=23
b=23.0
print(a is not b)"""

'''a=23
b=a
#a=23
#b=23
print(a == b)'''

#find value of X, Y, Z:

a = 9
b = 12
c = 3

#x = a - b / 3 + c * 2 - 1
#x = 9 -12 / 3 + 3 * 2 - 1
#print(x)

#y = a - b / (3 + c) * (2 - 1)
#y = 9 - 12 / (3 + 3) * (2 - 1)
#print(y)

z = a - (b / (3 + c) * 2) - 1
z = 9 - (12 / (3 + 3) * 2) - 1
print(z)