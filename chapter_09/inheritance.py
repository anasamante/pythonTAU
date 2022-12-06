"""Inheritance when we use the attributes and methods from the parent class and make them available to the child's
class. in order for the child's class to use those methods the super method is used, we can set any new attributes in
the child's class. """
import random


# example Person class
class Person:
    def __init__(self, firstname, lastname, health, status):

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        print("Hi, I'm {} {}.".format(self.firstname, self.lastname))

    def emote(self):
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


Maria = Person("Maria", "Gutierrez", 95, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 22, status=True)


# example child class Enemy
class Enemy(Person):
    """all attributes, inherited and new, the methods created below are not available on the person class"""
    def __init__(self, weapon, firstname, lastname, health, status):
        """Use the super method, to initialize attributes of the parent class"""
        super().__init__(firstname, lastname, health, status)
        """the attribute is new in the Enemy Object"""
        self.weapon = weapon

    def introduce(self):
        print("You are my mortal enemy!!!")

    def hurt(self, other):
        """The self argument allows access to the enemy and the “other” allows access to the other person that I am
        interacting with. """
        if self.weapon == "rock":
            other.health -= 10
        elif self.weapon == "stick":
            other.health -= 5
        print("{} health is {}".format(other.firstname, other.health))

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.firstname))

    def steal(self, other):
        print("ha ha ha, {}, I have your stuff! {}".format(other.firstname, other.status))
        if other.status == True:
            other.status = False
        print("{}, {}".format(other.firstname, other.status))


Alex = Enemy("rock", "Alex", "Wayne", 75, status=False)
Alex.introduce()
Alex.hurt(Maria)
Alex.insult(Lee)
Alex.steal(Maria)