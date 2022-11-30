"""Classes. - allows to group data and information like variables and functions into a single organized unit. - can
be organized one to a file, or multiple similar classes into the same file. Features - allow us to share information
with other classes and with other parts of the program. - inheritance which allow us to borrow from one class and use
its elements to create another one. - multiple inheritance which allows a class to inherit attributes from multiple
classes. - inherited or derived classes can override the parent classes - all classes in Python are Objects. -
information inside a class are usually functions, but can also contain variables that are specific to the class
and usable throughout the entire class. - instance variables  are specific to any Objects that are created by the
class.

The init method - allows every instance of a class to be initialized with specific parameters pre-determined at the
creation of that Object. - sets the attributes for the Object, the characteristics, the given parameters are
available to every class method.

The self variable - allows information to be shared easily and efficiently. - represents an instance of a class,
and it references the instance of the class that has been created. - We use self in order to make available all the
attributes to the methods throughout the class. - if a method is running as a part of the class rather than as an
instance of the class, then we do not need to use the self parameter in the method. """
import random


class Person:

    def __init__(self, firstname, lastname, health, status):
        """ initialize attributes to be used in all class methods, and for class Objects created by this class. """
        """We'll assign each characteristic to the name self. and then the name of the attributes, it allow those 
        characteristics to be available in our __init__ method as well as in the other methods. You'll notice that 
        every method that we have in the class has self as the first argument, and this is the reason why. """

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        """ class methods: we only have to write this method once, but it can be used by every individual Object that
        we create with our class. """
        """ All people introduce themselves"""
        print("Hi, I'm {} {}.".format(self.firstname, self.lastname))

    def emote(self):
        """ method that prints a message based on the health score of the person that we create."""
        """ The method will use the Python random module and using that random module we’ll assign an emotion to our 
        person based on the random number that is chosen using conditional statements. """
        emotion = random.randrange(1, 3)

        if emotion == 1:
            print("{} is happy today".format(self.firstname))

        elif emotion == 2:
            print("{} is sad today".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print("{} is fully healthy!".format(self.firstname))
        elif self.health >= 76:
            print("{} feels tired.".format(self.firstname))
        elif self.health >= 51:
            print("{} feels unwell.".format(self.firstname))
        elif self.health >= 40:
            print("{} goes to the doctor.".format(self.firstname))
        else:
            print("{} is unconscious.".format(self.firstname))


"""we will instantiate or make different people using this class. We'll give the class name Person, and then you'll 
notice that the arguments come up to remind us of all the different attributes that are available for us to use and 
define. """
Maria = Person("Maria", "Gutierrez", 60, status=True)
Rey = Person("Rey", "Jones", 50, status=False)
Lee = Person("Lee", "Williams", 22, status=True)

print("{} is my friend? {}".format(Rey.firstname, Rey.status))
print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is my friend? {}".format(Lee.firstname, Lee.status))

Maria.introduce()
Rey.introduce()
Lee.introduce()

Maria.status_change()
Rey.status_change()
Lee.status_change()

Maria.emote()
Rey.emote()
Lee.emote()
