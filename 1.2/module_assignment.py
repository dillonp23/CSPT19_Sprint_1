
# CodeSignal Assignment 1.2

"""
Exercise 1:

Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the array, return -1.

*Example:
    csWhereIsBob(["Jimmy", "Layla", "Bob"]) ➞ 2

Notes:
    Assume all names start with a capital letter and are lowercase thereafter (i.e. don't worry about finding "BOB" or "bob").
"""

def csWhereIsBob(names):

    for index in range(len(names)):
        if names[index] == "Bob":
            return index
    
    return -1

print(csWhereIsBob(["Jimmy", "Layla", "Bob"])) # expected: => 2
print(csWhereIsBob(["Bob", "Layla", "Kaitlyn", "Patricia"])) # expected: => 0
print(csWhereIsBob(["Jimmy", "Layla", "James"])) # expected: => -1
print(csWhereIsBob([""])) # expected: => -1
print(csWhereIsBob([])) # expected: => -1