'''Q1'''
class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_speed):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_speed = average_speed
car = Vehicle("Tesla Model S", 250, 120)
print(car.name_of_vehicle)  # Output: Tesla Model S
print(car.max_speed)  # Output: 250
print(car.average_speed)  # Output: 120

'''Q2'''
class Car(Vehicle):
    def seating_capacity(self, capacity):
        return f"The {self.name_of_vehicle} has a seating capacity of {capacity} people."
car = Car("Tesla Model S", 250, 120)
capacity = 4
print(car.seating_capacity(capacity))  # Output: The Tesla Model S has a seating capacity of 4 people.

'''Q3'''
'''Multiple inheritance is a feature in object-oriented programming languages that allows a class to 
inherit attributes and methods from more than one parent class. It enables a subclass to inherit and 
combine the functionalities of multiple parent classes.'''
class Vehicle:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Vehicle:", self.name)


class Engine:
    def start_engine(self):
        print("Engine started.")


class Car(Vehicle, Engine):
    def __init__(self, name, color):
        Vehicle.__init__(self, name)
        self.color = color

    def display_color(self):
        print("Color:", self.color)


car = Car("Tesla Model S", "Red")
car.display_name()    # Output: Vehicle: Tesla Model S
car.display_color()   # Output: Color: Red
car.start_engine()    # Output: Engine started.

'''Q4'''
'''In Python, getters and setters are methods that are used to access and modify the values of class 
attributes (variables) in a controlled manner. They provide a way to encapsulate attribute access and 
ensure data integrity.
A getter method, also known as an accessor method, is used to retrieve the value of an attribute. 
It typically has the prefix "get_" followed by the attribute name.
A setter method, also known as a mutator method, is used to set or modify the value of an attribute. 
It typically has the prefix "set_" followed by the attribute name.'''
class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name
person = Person("John Doe")
print(person.get_name())  # Output: John Doe

person.set_name("Jane Smith")
print(person.get_name())  # Output: Jane Smith

'''Q5'''
'''Method overriding in Python is a concept in object-oriented programming where a subclass provides a 
different implementation of a method that is already defined in its parent class. It allows the subclass 
to modify the behavior of the inherited method according to its specific needs.'''
class Vehicle:
    def start_engine(self):
        print("Engine started.")


class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")


class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started.")


car = Car()
car.start_engine()  # Output: Car engine started.

motorcycle = Motorcycle()
motorcycle.start_engine()  # Output: Motorcycle engine started.
