
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




"""
Exercise 2

A palindrome is a word, phrase, number, or another sequence of characters that reads the same backward or forward. This includes 
capital letters, punctuation, and other special characters.

Given a string, write a function that checks if the input is a valid palindrome.

Examples:
    csCheckPalindrome("racecar") -> true
    csCheckPalindrome("anna") -> true
    csCheckPalindrome("12345") -> false
    csCheckPalindrome("12321") -> true

* Notes:
- Try to solve this challenge without using the reverse of the input string; use a for loop to iterate through the string and 
make the necessary comparisons.
- Something like the code below might be your first intuition, but can you figure out a way to use a for loop instead?

    def csCheckPalindrome(input_str):
        return input_str == "".join(reversed(input_str))
"""