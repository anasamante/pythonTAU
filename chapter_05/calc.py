"""While Loop in Calculator"""
"""we're going to create our own “on button”. when we ran our calculator function the first time it ran once and then 
it ended, we want to make sure that like a real calculator, our users can use the calculator repeatedly if they need to. 
So, we'll add a while loop here and we can just say while on."""

on = True


def add():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a + b)


def subtraction():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a - b)


def multiply():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a * b)


def divide():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a / b)


# enclose selection into while loop
while on:
    operation = input("Please type +, -, *, / or q: ")
    if operation == "+":
        add()
    elif operation == "-":
        subtraction()
    elif operation == "*":
        multiply()
    elif operation == "/":
        divide()
    elif operation == "q":
        on = False
    else:
        print("That operation is not available.")
