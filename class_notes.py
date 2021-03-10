"""

# Mutable vs Immutable

Functions in python are either passing by value, or passing by reference depending on
the data type.

1. Pass by value (immutable) -> booleans, tuples, numbers (int/float),

2. Pass by reference (mutable) -> 

When passing by value, we are passing a copy of the original data, the new 
    variable represents a new space in memory, so the original variable 
    remains the same -> *Example 1 below*



"""

# Example 1 - Pass by reference w/booleans #

def make_false(some_variable):
    some_variable = False
    return some_variable

a = True
b = 1

make_false(a)
make_false(b)

print(a)
print(b)


"""
Control flow in Python
    - if/elif/else blocks
    - and/or operators
"""

def do_things(num):
    if num == 1:
        print("foo")
    elif num == 2:
        print("bar")
    else:
        print("foobar")

do_things(1)
do_things(2)
do_things(3)