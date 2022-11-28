"""Dictionaries: data collection stores data in key/value pairs.
The keys are made of Strings, integers, or tuples, and need to be both unique and immutable.
The values can be set to any data type.
any number of key/value pairs can be contained in a dictionary.
empty dictionary: assign a dictionary name with nothing in the curly braces
your dictionary can contain millions of entries.
are mutable and can be changed using the methods.
As of Python 3.7, the order of a dictionary can be maintained.
Dictionaries are created with curly braces and each key is separated from each value by a colon.
Each key/value pair is separated from each other key/value pair with a comma.
"""

"""Python Dictionary Methods
.get we can find the value of any key in the dictionary
"""

stuff = {"food": 15, "energy": 100, "enemies": 3}
print(stuff.get("food"))  # will return 15

"""Python Dictionary Methods
.items takes the name of the dictionary and outputs a view of the key/value pairs
"""

print(stuff.items())  # this print the entire dictionary

"""Python Dictionary Methods
.keys returns a view of all of the keys in the dictionary
"""

print(stuff.keys())  # this prints the keys of the dictionary

"""Python Dictionary Methods
.popitem allows us to remove the last item in a dictionary.
"""

print(stuff.popitem())
print(stuff)  # enemies pair was removed

"""Python Dictionary Methods
.setdefault allows us to see what the value is of a key that is in the dictionary, and
 allows us to set a default value when a key is not in the dictionary and to add that value to the dictionary.
"""

print(stuff.setdefault("food"))  # this will return 15
print(stuff.setdefault("friends", 123))  # this will add friends to the dict

print(stuff)

"""Python Dictionary Methods
.update updates the first dictionary with another dictionary. update specified key/pair
"""

new_items = {"rocks": 4, "arrows": 15}
stuff.update(new_items)  # add new items dict to stuff dict
print(stuff)

up_new = {"food": 2, "energy": 2}
stuff.update(up_new)  # updates the key/pair food and energy
print(stuff)  # prints food 2 and energy 2

stuff.update(food=450, energy=6)  # updates the key/pair food and energy does not require a 2nd dict
print(stuff)  # prints food 450 and energy 6
