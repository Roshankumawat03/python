# What is a Dictionary?

# A dictionary is an unordered collection of items. Each item is stored as a key-value pair.
#     Unordered : Historically, dictionaries were unordered. From Python 3.7 onwards, dictionaries maintain insertion order.
#     Mutable: You can add, remove, and modify key-value pairs after the dictionary has been created.
#     Values can be anything: Values can be of any data type and can be duplicates.
#     Mapping: Dictionaries are often referred to as "mappings" because they map keys to values.
#     We use the : operator to separate the key and value

  
# An empty dictionary
# empty_dict = {} # dict()
# print(empty_dict)

# # # A dictionary with string keys and various values
# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# print(person)

# # A dictionary with mixed key types (valid because all are immutable and unique)
# mixed_keys_dict = {
#     "name": "Bob",
#     1: "one",
#     3.14: "pi",
#     (1, 2): "tuple key"
# }
# print(mixed_keys_dict)


# # Creating a dictionary using the dict() constructor 
# Note If you are using the dict method you can only pass the strings as key
# student = dict(
#     name="Charlie",
#     id=101,
#     grade="A"
# )
# print(student)


# Accessing Values
# a = {"name": "Alice", "age": 30, "city": "New York"}
# print( a[ "city" ] )

# a = { 
#     "name": "Alice",
#     "age": 30,
#     "city": "New York",
#     "data1": { 
#         "level": "Advanced",
#         "data2": [ 1, 2, 3, 4, 5, { "data3": "dummy_value" } ]
#     }
# }

# print( a[ "data1" ][ "data2" ][-1]["data3"] )
# print( a.get("agee") )

# # Accessing with a default value
# print( a.get("city", "Unknown") )

# Modifying Dictionaries
# grades = {"math": 90, "science": 85}
# print(grades)
# grades["history"] = 78
# print(grades)
# grades["math"] = 40
# print(grades)

# Delete a key-value pair using del
# del grades["science"]
# print(grades) # Output: After del 'science': {'math': 90}

# a = [ 1, 2, 3]
# del a[-1]
# print(a)

# Pop an item
# popped_value = grades.pop("math")
# print(popped_value)
# print(grades)

# # Pop a non-existent item with a default
# missing_value = grades.pop("english", "Not found")
# print(missing_value) # Output: Not found

# Pop an arbitrary item (Python 3.7+ is last inserted)
# grades = {"math": 90, "science": 85}
# grades["art"] = 95
# grades["music"] = 88
# print(f"Before popitem: {grades}")
# popped_item_pair = grades.popitem()
# popped_item_pair = grades.popitem()
# print(f"Popped item pair: {popped_item_pair}, After popitem: {grades}")

# grades.clear()
# print(grades)


# profile = {
#     "name": "Bob",
#     "age": 25,
#     "gender": "Male"
# }

# Length
# print(len( profile ))

# Membership (checks for key)
# print('name' in profile)
# print('Bob' in profile)


# Dictionary Methods

# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}
# d1.update(d2)
# print(f"After update: {d1}") # Output: After update: {'a': 1, 'b': 3, 'c': 4}

# d2.update(d1)
# print(d2)

# data = {"name": "Alice"}
# email = data.setdefault("email", "unknown@example.com")
# print(data, email)


# data = list(range(1, 51))

# counter = 0
# while counter < len(data):
#     data[counter] = "key" + str(data[counter])
#     counter += 1

# print(data)
# new_dict = dict.fromkeys(["key1", "key2", "key3"], 0)
# print(new_dict)

# new_dict = dict.fromkeys(data, 50)
# print(new_dict)

# company = {
#     "CEO": {
#         "name": "John Doe",
#         "department": "Executive"
#     },
#     "employees": {
#         "101": {
#             "name": "Alice",
#             "role": "Engineer"
#         },
#         "102": {
#             "name": "Bob",
#             "role": "Designer"
#         }
#     },
#     "departments": ["HR", "Engineering", "Design"]
# }

# print( company["employees"]["101"]["name"] )

# person = { "name": "Alice", "age": 30, "city": "New York" }

# data = tuple(person.values())
# data1 = tuple(person.keys())
# data2 = person.items()


# print(data)
# print(data1)
# print(list(data2))

# Intermediate Level: More Dictionary Manipulations & Concepts


person = { "name": "Alice", "age": 30, "city": "New York" }


# for x in person:
#     print(x)

# for x in person.values(): # for x in dict_values(['Alice', 30, 'New York']):
#     print(x)

data = [('name', 'Alice', 1), ('age', 30, 2), ('city', 'New York', 3)]

# for x, y, z in data:
#     print( f"x is {x} and y is {y} and z in {z}")


# for x, y in person.items():
#     print( f"x is {x} and y is {y}")


# From a list of (key, value) tuples
# countries = dict([("USA", "Washington"), ("France", "Paris")])
# print(f"Countries dictionary (dict() with list of tuples): {countries}") # Output: Countries dictionary (dict() with list of tuples): {'USA': 'Washington', 'France': 'Paris'}


