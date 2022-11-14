""" A loop is a useful construct for when you'd like to repeat the same actions any number of times.

For Loops: useful when you'd like to iterate over each item in a list. Allows you to repeat your action for every
item in the list or for a specified number of items in the list """

fruits = ["apple", "orange", "pears", "cherries", "grapes"]

for i in fruits:
    print("Would you like {}?".format(i))

""" Another example of a for loop that we can try is looping over a range of numbers. Range function built-in Python 
function, we can assign the range by assigning the first number, a comma, and then assigning the ending number. The 
ending number is not included. """

for number in range(1, 11):
    print("Number: {}".format(number))

""" While Loops: will run any time a condition remains true. """

temp_f = 40  # set a temperature in Fahrenheit to 40 degrees
while temp_f > 32:  # while the temperature is greater than 32 degrees, we can print a message.
    print("The water is {} degrees.".format(temp_f))
    temp_f -= 1  # if this is not added, we have an init loop. all that does is decrease the variable in one

""" Loop Control: Python includes break, continue, and pass.
# break: indicates the loop should ends and go on to the next statement outside of the loop.
# continue: skips the current part of the loop and moves on to the next part of the loop.
# pass: skips any part of the loop, this is best used for testing code.
"""

# break:
temp_f = 40
while temp_f > 32:
    print("the water is {} degrees.".format(temp_f))
    temp_f -= 1
    if temp_f == 33:
        break  # once the temp became equal to 33, the print statement stopped printing and the loop stopped running.

# continue:
for i in range(1, 11):
    if i == 7:
        print("Skipping #7")
        continue
    print("This is the number: {}.".format(i))

# Where our break statement ended the loop completely once the if condition was met, the continue statement does
# whatever is needed when the if condition is met but then continues the rest of the loop.

# pass:
for i in range(1, 11):
    if i == 3:
        pass  # the number 3 is skipped completely, there is no print statement for the number 3.
    else:
        print("The number is {}.".format(i))
