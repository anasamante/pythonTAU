"""
work with args and kwargs, or arguments and keyword arguments

Positional Arguments
doing my function definition and giving the arguments. added comment to explain what the function does.
the function and it took all of our variables from the argument and input them. we get an error if missing
arguments that the function expects.
These are positional arguments because Python is reading these arguments_ in order_, in the position that they are given
in the function definition.
"""


def user_info(name, age, city):
    """This function prints name, age, and city from an argument provided to the function."""

    print("{} is {} years old, from {}".format(name, age, city))


user_info("Janet", 58, "Oklahoma City")

""" Keyword Arguments 
overcome limitations of positional arguments, 
we have many arguments that we would like to provide to a function but we don't necessarily need to provide everything. 
we can set some defaults when we're using keyword arguments, so function knows what if we don't provide the all arguments.
So, since we have default for both age and city, we can go ahead and test to ensure that this is working as expected 
by providing a name argument and leaving the other 2 arguments blank. 
 you don't need to follow the positional order of the argument."""


def user_info(name, age=0, city="Tucson"):
    """This function prints name, age, and city, age and city are keyword arguments"""

    print("{} is {} years old, from {}".format(name, age, city))


user_info("Ana")
# overwriting keyword argument age
user_info(age=35, name="Tati")

"""
*args & **kwargs
*args allows a function to take any number of positional arguments.
**kwargs allows a function to take any number of keyword arguments.
Any required arguments that you wish to pass into a function, must be passed before *args and **kwargs.
 the fname, lname, email, and company formal positional arguments followed by the *args and **kwargs.
When we use the function, start with the required arguments. Then pass  a *arg as a salary
and a **kwarg as the hire date.
"""


def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}. her salary is {}, and she was hired on {}".format(fname, lname, email, company, args, kwargs))


application("Jess", "Ingrass", "mail @ mail.com", "Teach Code", 75000, hire_date="September 2010")
