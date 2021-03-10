"""

# Mutable vs Immutable

Functions in python are either passing by value, or passing by reference depending on
the data type.

1. Pass by value (immutable) -> booleans, tuples, numbers (int/float)

2. Pass by reference (mutable) -> lists

When passing by value, we are passing a new copy of the original data, the new 
    variable represents a new space in memory, so the original variable 
    remains the same -> *Example 1 below*


When passing by reference, we are passing a reference to the original object in
    memory. Therefore, mutable objects that are passed by reference into functions can 
    be modified. Changing an object within the scope of a function, will change the
    object outside of the scope of the function as well. -> *Example 2 below*
"""

# Example 1 - Pass by value w/booleans #

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


"""
Lists in Python

- arrays
- sequential data
- loosley-typed store heterogenous data
- lists are mutable, i.e. pass by reference (vs. pass by value)
- fast indexing and appending/removing items at end of list
- can get sublists with slicing
- lists are dynamically sizing arrys, list are built on arrays
"""

# Example 2 - Pass by reference (using mutable objects)

my_list = []

# Use .append(newItem) to add to end of list
my_list.append(True)
my_list.append(1)
print(my_list)

def change_list(some_list):
    some_list.append("new item")

print(my_list)
change_list(my_list)
print(my_list)

my_list = [1,2,3,4,5,6,7]
print(my_list)

# Use .pop() method to remove AND return last element of the list
print(my_list.pop())
print(my_list)

# List slicing can be used to return a new copy of a sublist from original
# Remember immutable vs. mutable here, SLICING RETURNS a NEW COPY - see below
def slice_list(some_list):
    return some_list[:-1]

slice_list(my_list)
new_slice = slice_list(my_list)

print(my_list)
print(new_slice)

