# What is a Class?
# A class is a blueprint or a template for creating objects.
# Think of a class as a set of instructions for building something, like the blueprint for a house. 
# The blueprint defines what the house will have—rooms, doors, windows—but it isn't the house itself.

# In Python, a class defines the attributes (data) and methods (behaviors) that all objects of that class will share.
#     Attributes: These are the data or properties of an object. For a Car class, attributes could be color, brand, and mileage.
#     Methods: These are functions that an object can perform. For a Car class, methods could be start_engine(), drive(), or honk_horn().

# Defining a Class
# You define a class using the class keyword, followed by the class name (which, by convention, should start with a capital letter).

# class ClassName:
#     # Class body (attributes and methods)
#     pass # 'pass' is a placeholder for an empty class


# def bark():
#         print("Woof!")

# class SocialMedia:   

#     CEO = "Mark"

#     def like():
#         print("Liked")

#     def comment():
#         print("Commented")

# # bark()
# # Dog.bark()



# # Creating Objects (Instances) from a Class

# # object_name = ClassName()

# Insta = SocialMedia()
# LinkedIn = SocialMedia()
# Twitter = SocialMedia()
# LinkedIn.CEO = "Ryan"
# Twitter.CEO = "Alan"

# print( Insta.CEO )
# print( LinkedIn.CEO )
# print( Twitter.CEO )

class car:

    color = "Black"
    brand = "Royals Roy"
    milage = "3mph"

    def engin(self):
        print("RR Engin.")
    
    def drive(self):
        print("Driving")

    def Honk(self):
        print("Peeeeeeeeeeeeeeeeee")


a = car()
# b = car()

# print(a)
# print(b)

# b.brand = "Honda"
# b.milage = "25mph"

# print(a.brand)
# print(b.brand)
# print(a.Honk())


# Attributes (The "What It Is")
# Attributes are the data or properties associated with an object.
# They store information about a specific instance. 
# Think of them as variables that belong to an object.

# Methods (The "What It Can Do")
# Methods are the functions that belong to a class.
# They define the behaviors or actions an object can perform.
# They are essentially functions that are defined within a class.

# print( dir(a) )

# class Dog:

#     species = "JS"

#     def __init__(self):
#         print("Bhaiya Object Ban gaya h.")
#         self.b = 44

#     def bark(self):
#         print(self.b)
#         self.c = 23
#         print(f"says woof!")

#     def eat(self):
#         print(self.c)
#         print(f"hungry right now.")

# a = Dog()
# a.bark()
# a.eat()
# print(dir(Dog))
