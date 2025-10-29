# Create a function that sorts a list and removes all duplicate items from it.
# Examples

# Output Should Look Like this:
# setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]
# setify([4, 4, 4, 4]) ➞ [4]
# setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]
# setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]

def setify(list):
    return sorted(set(list))

print(setify([1,3,3,5,5]))
print(setify([4,4,4,4]))
print(setify([5,6,7,8,9,15,11,10]))
print(setify([3,3,3,2,1]))