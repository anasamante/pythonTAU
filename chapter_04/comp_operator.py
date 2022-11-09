"""Comparison Operators are ways for us to make comparisons between one or more items in any of our programs.
Boolean's True and False are keywords in Python.
"""
print(1 < 1)
print(1 > 1)
print(1 == 1)
print(1 >= 1)
print(1 <= 1)
print(1 != 1)


"""Control Structures: if, elif, else If, else/if and else — if, elif and else — are control structures in Python. 
The if statement, used by itself, shows code that should run only if certain conditions are met The elif statement 
shows code that should run when conditions before are not met, and many conditions could possibly be met. The elif 
code is run in the order that it appears else statements don't have any condition attached to them. elif statement 
that agrees with a condition, but there's another condition that also agrees at the same time, once the condition is 
met, none of the other conditions matter """

name = input("What's your name? ")
if name == "Jessica":
    print("Hello, nice to see you {}".format(name))

elif name == "Danielle":
    print("Hello, you are a great person!")

elif name == "Kingston":
    print("Hi, {}, let's have lunch soon!".format(name))

else:
    print("Have a nice day.")

