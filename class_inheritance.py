# What is Inheritance? 

# Inheritance is a fundamental concept in Object-Oriented Programming (OOP) 
# that allows a new class to inherit attributes and methods from an existing class.
# Think of it like a family tree. A child class (the subclass or derived class)
# inherits traits (attributes and methods) from its parent class (the superclass or base class). 
# The subclass can then add its own unique traits or override the inherited ones.
# The Basics of Inheritance

# To create a subclass, you define a new class with the parent class name in parentheses.
# class Parent:
#     pass

# class Child(Parent):
#     pass

# class Vehicle:

#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def display_info(self):
#         print(f"Brand: {self.brand}, Color: {self.color}")

# class Car( Vehicle ):
    
#     def wheels(self):
#         print("Car has 4 wheels")

# my_car = Car("Honda", "White")
# print(my_car.brand)

# super(): Accessing the Parent Class
# The super() function is a special tool used to call methods from the parent class. This is particularly useful when the child class has its own __init__ method and you want to reuse the parent's initialization code.

# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#         print("Vehicle __init__ called.")

# class Car(Vehicle):
#     def __init__(self, num_wheels):
#         self.num_wheels = num_wheels
#         print("Car __init__ called.")
#         super().__init__("Honda", "White")

#     def car_info(self):
#         print(f"This is a {self.color} {self.brand} with {self.num_wheels} wheels.")


# my_car = Car(4)
# print(my_car.num_wheels)
# my_car.car_info()

# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#         print("Vehicle __init__ called.")

# class Car(Vehicle):
#     def __init__(self, num_wheels):
#         self.num_wheels = num_wheels
#         print("Car __init__ called.")

#     def set_car_brand_and_color(self, brand, color):
#         super().__init__(brand, color)

#     def car_info(self):
#         print(f"This is a {self.color} {self.brand} with {self.num_wheels} wheels.")

# my_car = Car(num_wheels=4)
# my_car.set_car_brand_and_color(brand="Ford", color="Red")
# my_car.car_info()


# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#         print("Vehicle __init__ called.")

# class Car(Vehicle):
#     def __init__(self, brand, color, num_wheels):
#         self.num_wheels = num_wheels
#         print("Car __init__ called.")
#         super().__init__(brand, color)

#     def car_info(self):
#         print(f"This is a {self.color} {self.brand} with {self.num_wheels} wheels.")

# my_car = Car(brand="Ford", color="Red", num_wheels=4)
# my_car.car_info()

# Method Overriding

# Method overriding is when a subclass provides its own specific implementation
# of a method that is already defined in its parent class.
# The method in the subclass "overrides" the one in the superclass.

# class Vehicle:
#     def display_info(self):
#         print("This is a generic vehicle.")

# class Car(Vehicle):
#     # This method overrides the one in the parent class
#     def display_info(self):
#         print("This is a specific car.")

# class Boat(Vehicle):
#     # This class inherits and does not override the method
#     pass

# my_car = Car()
# my_boat = Boat()

# my_car.display_info() # Calls the overridden method in Car
# my_boat.display_info() # Calls the inherited method from Vehicle
