
# CodeSignal Assignment 1.2

"""
Exercise 1:

Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location 
in the list. If Bob is not in the array, return -1.

* Example:
    csWhereIsBob(["Jimmy", "Layla", "Bob"]) ➞ 2

Notes:
    Assume all names start with a capital letter and are lowercase thereafter 
        - (i.e. don't worry about finding "BOB" or "bob")
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



"""
Exercise 2: 

Imagine a school that children attend for years. In each year, there are a certain number of groups 
started, marked with the letters. So if years = 7 and groups = 4:
    - First year the groups are: 1a, 1b, 1c, 1d
    - Last year the groups are: 7a, 7b, 7c, 7d.

Write a function that returns the groups in the school by year (as a string), separated with a comma and space in the form of "1a, 1b, 1c, 1d, 2a, 2b (....) 6d, 7a, 7b, 7c, 7d".

* Example:
    csSchoolYearsAndGroups(years = 7, groups = 4) ➞ "1a, 1b, 1c, 1d, 2a, 2b, 2c, 2d, 3a, 3b, 3c, 3d, 4a, 4b, 4c, 4d, 5a, 5b, 5c, 5d, 6a, 6b, 6c, 6d, 7a, 7b, 7c, 7d"

* Constraints:
    1 <= years <= 10
    1 <= groups <=26
"""
import string

def csSchoolYearsAndGroups(years, groups):
    count = 0
    alphabet = string.ascii_lowercase
    
    result_list = []
    separator = ", "

    # use for loop with range 1 up to "years"
    # use a reference to lookup alphabet letter based on "groups" input
    for year in range(1, years+1):
        while count != groups:
            combo = f"{year}{alphabet[count]}"
            result_list.append(combo)
            count += 1
            
        count = 0
    
    return separator.join(result_list)


print(csSchoolYearsAndGroups(5, 3))
print(csSchoolYearsAndGroups(7, 4))
print(csSchoolYearsAndGroups(1, 8))
print(csSchoolYearsAndGroups(8, 7))
print(csSchoolYearsAndGroups(2, 2))

# Expected behavior:
# csSchoolYearsAndGroups(years = 7, groups = 4) => "1a, 1b, 1c, 1d, 2a, 2b, 2c, 2d, 3a, 3b, 3c, 3d, 4a, 4b, 4c, 4d, 5a, 5b, 5c, 5d, 6a, 6b, 6c, 6d, 7a, 7b, 7c, 7d"



"""
Exercise 3:

Create a function that concatenates the number 7 to the end of every chord in a list. If a chord already ends with a 7, ignore that chord.

* Examples:
    csMakeItJazzy(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]

* Notes:
    - Return an empty list if the given list is empty.
    - You can expect all the tests to have valid chords.
"""

# def csMakeItJazzy(chords):
#     # iterate list and add 7 anything that doesn't end in 7
#     # use string splicing to get last character, if not 7, then append it
#     jazzy_chords = []
    
#     for chord in chords:
#         if chord[-1] != "7":
#             chord += "7"
        
#         jazzy_chords.append(chord)
    
#     return jazzy_chords


def csMakeItJazzy(chords):
    # n = letter for note in chord
    return [f"{n}7" if n[-1] != "7" else n for n in chords]


# # Would never actually do this, but just as a fun example:
# def csMakeItJazzy(chords):
#     # n = letter for note in chord
#     return [(lambda n: f"{n}" if chords[-1] != "7" else n)(n) for n in chords]


print(csMakeItJazzy(["G", "F", "C"]))
print(csMakeItJazzy(["Dm", "G", "E", "A"]))
print(csMakeItJazzy(["Dm", "G7", "E", "A"]))
print(csMakeItJazzy(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]))
print(csMakeItJazzy([]))



"""
Exercise 4:

Given a string of words, return the length of the shortest word(s).

* Notes:
- The input string will never be empty and you do not need to validate for different data types.
"""
# def csShortestWord(input_str):
#     word_list = input_str.split()
#     shortest_length = len(word_list[0])
    
#     # use the split built in string method to split words into list    
#     # iterate the spearated word list
#     for index in range(len(word_list)):
#         shortest_length = min(shortest_length, len(word_list[index]))

#     return shortest_length


def csShortestWord(input_str):
    return min([len(word) for word in input_str.split()])


print(csShortestWord("Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live")) # expected: 1
print(csShortestWord("not great programmer; just good programmer with great habits.")) # expected: 3
print(csShortestWord("Truth can only be found in one place: the code")) # expected: 2
print(csShortestWord("Give man program frustrate him for day Teach man program frustrate him for lifetime")) # expected: 3
print(csShortestWord("ZxuvWBoofsTUtasPIhsuCJjttHhBuuHZoxZk\tWZxAkjdCqDpML")) # expected: 13



"""
Exercise 5:
Given an array of integers, return the sum of all the positive integers in the array.

* Examples:
- csSumOfPositive([1, 2, 3, -4, 5]) -> 1 + 2 + 3 + 5 = 11

* Notes:
- If the input_arr does not contain any positive integers, the default sum should be 0.

"""

def csSumOfPositive(input_arr):
    # utilze a list comprehension:
    return sum([num for num in input_arr if num > 0])

print(csSumOfPositive([1, 2, 3, -4, 5])) # => 1 + 2 + 3 + 5 => expected: 11
print(csSumOfPositive([-3, -2, -1, 0, 1])) # => expected: 1
print(csSumOfPositive([-3, -2])) # => expected: 0



"""
Exercise 6:
Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum) of all integers in the range (except integers that contain the digit 5).

* Examples:
- csAnythingButFive(1, 5) -> 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)

* Notes:
- The output can contain the digit 5.
- The start number will always be less than the end number (both numbers can also be negative).
"""

def csAnythingButFive(start, end):
    # convert int to string and check if "5" in string
    # return length of resulting list

    return len([str(num) for num in range(start,end+1) if "5" not in str(num)])


# def csAnythingButFive_Loop(start, end):
#     nums = []

#     for num in range(start,end+1):
#         if "5" not in str(num):
#             nums.append(num)

#     return len(nums)

print(csAnythingButFive(1, 5))
print(csAnythingButFive(1, 9))
print(csAnythingButFive(4, 17))
print(csAnythingButFive(1, 90))

# csAnythingButFive(1, 5) => 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)
# csAnythingButFive(1, 9) => 1, 2, 3, 4, 6, 7, 8, 9 -> 8
# csAnythingButFive(4, 17) => 4,6,7,8,9,10,11,12,13,14,16,17 -> 12