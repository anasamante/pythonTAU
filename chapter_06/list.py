"""
List: list is a collection of items.
can be of any data type
the items contained in a list can even be other lists, dictionaries, sets, tuples, or any mixture
are mutable, item can be retrieved, changed, rearranged, and acted upon
Lists maintain their order, it can access something by its position or index

List Methods:
*Append:
I can add a single item to the list
"""

fruits = ["peaches", "pears", "apples"]
years = [3, "1998", 2.5, 987, "1994"]

print(fruits, years)

fruits.append("banana")

print("Added banana {}".format(fruits))

"""
*Extend:
 allows us to extend the list with another list
"""

fruits.extend(years)
print("Added years list{}".format(fruits))

"""*Remove: taking an item out of a list. you need to make sure that you are actually using the exact item 
match that you want to remove """

fruits.remove("banana")

print("Removed banana {}".format(fruits))

"""*Pop: to remove an element by index. The index starts at 0 and most Python lists and Python counting begin at 
0. To access the last item in a list and you're not certain of the length of the list, you can use the concept of 
negative indexing, which starts at the end of a list. 

So, if I want to remove the last item, I can use fruits.pop(-1)."""

fruits.pop(0)

print("Removed peaches {}".format(fruits))

"""*Sort: can only be used with lists of like types """

numbers = [5, 1928, 4, 17, 68, 73.76, 20.458]
print("Not sorted numbers {}".format(numbers))

numbers.sort()
print("Sorted numbers {}".format(numbers))

"""
Checking Membership in a List
function called in and this function allows us to check the existence of an item in a list.
You can also check membership and the number of items with the count function.
We can also check membership as well as the index position using the index function.
"""
second_fruit = ["peaches", "apples", "pears", "apples", "apples"]
second_years = [3, "1998", 2.5, 987, "1994"]

print("apple" in second_fruit)  # this will return False, it is not an exact match
print("apples" in second_fruit)  # this will return True
print(second_fruit.count("apples"))  # this will return 3 item is there 3 times
print(second_fruit.count("apple"))  # this will return 0 the item does not exist
print(second_fruit.index("apples")) # this will return 1, The first instance of “apples” appears as the second item
# in the list.
