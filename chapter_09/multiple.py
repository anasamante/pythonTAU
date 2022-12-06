""" Multiple Inheritance: when one class inherits from multiple classes and is able to use attributes and methods
from both. ability to reuse small amounts of code in multiple classes. the order of inheritance matters. can become
quite complicated depending on the number of classes, the names of class methods and other factors, including common
attributes shared among multiple parent classes. There can be more maintenance involved when refactoring code that is
using multiple inheritance. if we have multiple classes that we want to inherit from, we'll have the attributes of
each class and then bring in the attributes of the class individually into the initialization or __init__ method of
the child class."""


# Parent class 1
class Item():
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}.".format(self.sku))


# Parent class 2
class Garment():
    def __init__(self, section, model):
        self.section = section
        self.model = model

    def print_garment(self):
        print("The garment is in section {}, {}.".format(self.section, self.model))


# Child Class
class Shirts(Item, Garment):
    def __init__(self, sku, section, model, name, color):  # define the attributes specific to the child's class
        self.name = name
        self.color = color
        Item.__init__(self, sku)  # initialize the attributes from parent class 1
        Garment.__init__(self, section, model)  # initialize the attributes from parent class 2

    def print_shirt(self):
        print("{} {} on sale!".format(self.color, self.name))


Blouse = Shirts("00001", 43, "Tops", "Formal Blouse", "White")

Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirt()
