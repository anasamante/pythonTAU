"""
A function is a unit of code that can be reused throughout a program.
Functions provide us re-usability and modularity throughout our code.

Parts of a Function:
Every Python function begins with def., a unique function name, the parenthesis and the colon.
The body of our function is always indented 4 spaces, and we remove the spaces when we want to call a function.
We'll use the unique name and the parenthesis to call the function.
"""


def addition():
    a = 10
    b = 30
    print(a + b)


# calls the function
addition()

"""
Getting User Input. a way to actually flexibly get user input. This is where our Python user input function can come in.

This prompt is always a String; and the input that goes into this prompt is also a String, 
so we'll need to do a little bit of magic with it to make it work in our calculator.
converted the String data into an integer by using int and wrapping that input function into an integer function.
"""


def addition_using_input():
    a = int(input("Enter a number. "))
    b = int(input("Please enter another number. "))
    print(a + b)


addition_using_input()
