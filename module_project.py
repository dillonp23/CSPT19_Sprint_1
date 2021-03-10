
# CodeSignal assignment for module 1.1 #

"""
Exercise 1: What are the steps in Lambda's U.P.E.R process?

1. Understand
2. Plan
3. Execute
4. Reflect
"""




"""
Exercise 2: What to do in the "Plan" step of UPER? (multiple choice question)

Create an actionable/easy to comprehend method of attacking the problem, often
using pseudocode to make sense of the problem

Tips:
    - identify issues or challenges and determine whether you need to go back 
    in order to the understand the problem and/or ask more questions in "U" step
"""




"""
Exercise 3: Create a function that returns True if the given string has any of the following:

-Only letters and no numbers.
-Only numbers and no letters.
-If a string has both numbers and letters or contains characters that don't fit into any category, return False.

Examples:

csAlphanumericRestriction("Bold") ➞ True
csAlphanumericRestriction("123454321") ➞ True
csAlphanumericRestriction("H3LL0") ➞ False
Notes:

Any string that contains spaces or is empty should return False.
[execution time limit] 4 seconds (py3)

[input] string input_str
[output] boolean
"""

def csAlphanumericRestriction(input_str):
    # Can use Python built in api to check if numeric or alpha
    # i.e. will return true if all numbers or all alpha in str
    if input_str.isnumeric() or input_str.isalpha():
        return True
    else:
        return False

print(csAlphanumericRestriction("123"))
print(csAlphanumericRestriction("abc"))
print(csAlphanumericRestriction("12c3"))

# Original solution below -> was unaware of the "isalpha()" method on str
    # def csAlphanumericRestriction(input_str):
    #     # Can use Python built in api to check if numeric
    #     # i.e. will return true if all numbers in str
    #     if input_str.isnumeric():
    #         return True
        
    #     # If not then iterate through characters and ensure all are letters
    #     # can use 'AND' keyword combining if statements
    #     # if char_in_str.isnumeric() == FALSE and char_in_str.isalnum()
        
    #     # Using this process will ensure that the characters are alphanumeric,
    #     # but will return False if a number is included
    #     for char in input_str:
    #         if char.isnumeric() == False and char.isalnum():
    #             continue
    #         else:
    #             return False
        
    #     return True




"""
Exercise 4: Write a function that takes a string as input and returns that string in reverse order, with the opposite casing for each character within the string.

Examples:

csOppositeReverse("Hello World") ➞ "DLROw OLLEh"
csOppositeReverse("ReVeRsE") ➞ "eSrEvEr"
csOppositeReverse("Radar") ➞ "RADAr"
Notes:

The input string will only contain alpha characters.
[execution time limit] 4 seconds (py3)

[input] string txt

[output] string
"""

def csOppositeReverse(txt):
    # Use string splicing with bracket syntax to return string in opposite order
    # Use the 'swapcase' method to switch from lower->upper and upper->lower
    return txt[::-1].swapcase()

print(csOppositeReverse("Hello World"))
print(csOppositeReverse("ReVeRsE"))
print(csOppositeReverse("Radar"))




"""
Exercise 5: Create a function that given an integer, returns an integer where every digit in the input integer is squared.

Examples:

csSquareAllDigits(9119) -> 811181 because 9^2 = 81, 1^2 = 1, 1^2 = 1, and 9^2 = 81
csSquareAllDigits(2483) -> 416649 because 2^2 = 4, 4^2 = 16, 8^2 = 64, and 3^2 = 9
[execution time limit] 4 seconds (py3)

[input] integer n

[output] integer
"""

def csSquareAllDigits(n):
    # convert the int into a string object
    # iterate through each character of the string and square it
    # use result to build new str, convert to int and return
    
    num_string = str(n)
    
    # can use list comprehension to reduce the functionality and number of steps
    return int("".join(str(int(char)**2) for char in num_string))

print(csSquareAllDigits(9119))




"""
Exercise 6: Given a string, return a new string with all the vowels removed.

Examples:

csRemoveTheVowels("Lambda School is awesome!") -> "Lmbd Schl s wsm!"
Notes:

For this challenge, "y" is not considered a vowel.
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] string
"""