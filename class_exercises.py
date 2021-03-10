
"""
Exercise 1: create a function that returns list of strings sorted alphabetically
"""

def sorted_list(lst):
    return sorted(lst)

list_1 = [8, 24, 94, 9, 1, 3, 7]
print(sorted_list(list_1))



"""
Exercise 2: Create a function that takes a string and checks if it has same number of x's and o's
- return boolean
- string can contain any character
- when no 'x' or 'o' return True
- make case-insensitive
"""

def XO(txt):
    x_count = 0
    o_count = 0

    for i in txt.lower():
        if i == "x":
            x_count += 1
        elif i == "o":
            o_count += 1

    return x_count == o_count

print(XO("xo"))
print(XO("XXoo"))
print(XO("xoX"))
print(XO("xoxo"))
print(XO("xOpsXOwqjxox"))
print(XO("abc"))

# The above works, but this is a much more consise way to accomplish the task 
# by using the Python api's
def XO_2(txt):
    txt = txt.lower()
    return txt.count("x") == txt.count("o")


print(XO_2("XO"))
print(XO_2("XXoo"))
print(XO_2("xoX"))
print(XO_2("xoxo"))
print(XO_2("xOpsXOwqjxox"))
print(XO_2("abc"))


"""
Create a function that applies a discount d to every number in the list

    * Tip: Use list comprehensions!
"""

def get_discounts(nums, percentage):
    # Convert discount to a number ignoring the percentage sign
    #  i.e. everything up to the last character which is "%"
    discount = int(percentage[:-1]) / 100
    return [n * discount for n in nums]

print(get_discounts([10, 20, 30, 40, 50, 60, 70], "10%"))
print(get_discounts([10, 20, 30, 40, 50, 60, 70], "30%"))
print(get_discounts([10, 20, 30, 40, 50, 60, 70], "40%"))
print(get_discounts([10, 20, 30, 40, 50, 60, 70], "90%"))