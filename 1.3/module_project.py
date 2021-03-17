
# Sprint 1.3 CodeSignal Assignment - Time & Space Complexity


"""
Exercise 1: Multiple Choice

Using Big O notation, what is correct classification of time complexity for the function below?

def do_lots_of_things(items):
    last = len(items) - 1 ## O(1) - constant
    print(items[last]) ## O(1) - constant

    middle = len(items) / 2 ## O(1) - constant
    i = 0 ## O(1) - constant

    while i < middle: ## O(n) - linear
        print(items[i]) ## O(1) - constant
        i += 1 ## O(1) - constant

    for num in range(100): ## O(1) - constant
        print(num) ## O(1) - constant


    ** Total: O(n) - linear **
"""



"""
Exercise 2: Multiple Choice

Using Big O notation, what is correct classification of space complexity for the function below?

def do_a_couple_things(n):
    my_list = [] ## O(1) - constant (initialization of empty space is constant relative to n for now)
    my_second_list = [0] * 26 ## O(1) - constant (remains same with growing input)

    for _ in range(n):
        my_list.append("lambda") ## O(n) - linear (increases proportionally to input size)
        print(my_second_list[n % 25]) ## O(1) - constant

    return my_list


    ** Total: O(n) - linear **
"""



"""
Exercise 3:

Given two strings that include only lowercase alpha characters, str_1 and str_2, write a function that 
returns a new sorted string that contains any character (only once) that appeared in str_1 or str_2.

* Examples:
    - csLongestPossible("aabbbcccdef", "xxyyzzz") -> "abcdefxyz"
    - csLongestPossible("abc", "abc") -> "abc"
"""

def csLongestPossible(str_1, str_2):
    str_1 += str_2
    str_1 = sorted(str_1)
    str_2 = ""
    
    for char in str_1:
        if char not in str_2:
            str_2 += char
            
    return str_2


print(csLongestPossible("aabbbcccdef", "xxyyzzz")) # expected: "abcdefxyz"
print(csLongestPossible("aretheyhere", "yestheyarehere")) # expected: "aehrsty"
print(csLongestPossible("loopingisfunbutdangerous", "lessdangerousthancoding")) # expected: "abcdefghilnoprstu"
print(csLongestPossible("inmanylanguages", "theresapairoffunctions")) # expected: "acefghilmnoprstuy"
print(csLongestPossible("etxtxgxqxkrwu", "fvaqjrvnzeyed")) # expected: "adefgjknqrtuvwxyz"
print(csLongestPossible("", "")) # expected: ""