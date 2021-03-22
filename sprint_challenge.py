
# Sprint 1 - Final Assessment

"""
Exercise 1

Given a string (the input will be in the form of an array of characters), write a function that returns the reverse of the given string.

* Examples:
    csReverseString(["l", "a", "m", "b", "d", "a"]) -> ["a", "d", "b", "m", "a", "l"]
    csReverseString(["I", "'", "m", " ", "a", "w", "e", "s", "o", "m", "e"]) -> ["e", "m", "o", "s", "e", "w", "a", " ", "m", "'", "I"]

* Notes:
    - Your solution should be "in-place" with O(1) space complexity. Although many in-place functions do not return the modified 
    input, in this case you should.
    - You should try using a "two-pointers approach".
    - Avoid using any built-in reverse methods in the language you are using (the goal of this challenge is for you to 
    implement your own method).
"""

def csReverseString(chars):
    last_index = len(chars) - 1
    
    for i in range(int(len(chars)/2)):
        temp = chars[i]
        chars[i] = chars[last_index]
        chars[last_index] = temp

        last_index -= 1


    return chars


print(csReverseString([]))
print(csReverseString(["a"]))
print(csReverseString(["a", "b"]))
print(csReverseString(["a", "b", "c"]))
print(csReverseString(["a", "b", "c", "d", "e"]))