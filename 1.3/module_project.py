
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