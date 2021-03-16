

"""
Sprint 1 Module 3: Time & Space Complexity


* Best Time & Space Complexitity *

    O(1): Constant
        - runtime is entirely unaffected by the input size 
        - excellent/ideal solution
        
        * example:
            - indexing element in array

    O(log n): Logarithmic 
        - as input size increases, rate of growth (acceleration) will decrease 
        - pretty good solution
        
        * example:
            - binary search in data sets

    O(n): Linear 
        - runtime will grow proportionally to input size
        - fair/average solution

        * example:
            - simple for loop iterating entire length of a list

    O(n log n): Quasilinear
        - runtime is a combination of linear and logarithmic
        - much worse than linear, but not quite as bad as polynomial
        - poor solution

    O(n^c): Polynomial
        - as input size increases, runtime will grow at a much faster rate
        - might work for small inputs but is not a scalable solution
        - very poor solution

        * common variations:
            - O(n^2): Quadratic
            - O(n^3): Cubic

        * example:
            - nested for loops where each loop is O(n)

    O(c^n): Exponential 
        - runtime grows exponentially as input size increases
        - very inefficient solution

    O(n!): Factorial
        - runtime grows at an astronomaically faster rate as input size increases
        - exceptionally inefficient/worst solution

* Worst Time & Space Complexitity *

"""



"""
Exercise 1: "136. Single Number" (https://leetcode.com/problems/single-number/)

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

* Example:
    Input: nums = [2,2,1]
    Output: 1

* UPER:
    if single element in nums, return element

    sort nums array
    store var for index
    store var for left (lhs) & right (rhs) hand side

    iterate through sorted nums list:
        set curr to nums[i]

        if index == 1 and lhs != curr
            return lhs

        if nums[i] != lhs and nums[i] != rhs, 
            return nums[i]

        else it means nums[i] == lhs or rhs
            update lhs
            iterate i
            update rhs
"""

def findSingleNumber(nums):
    if len(nums) == 1:
        return nums[0]
        
    nums.sort()

    i = 1
    lhs = nums[0]
    rhs = nums[i+1]

    while i < len(nums):
        curr = nums[i]
            
        if i == 1 and lhs != curr:
            return lhs

        if curr != lhs and curr != rhs:
            return curr
        else:
            lhs = curr
            i += 1

            try:
                rhs = nums[i+1]
            except:
                rhs = None


# def findSingleNumber_BitwiseXOR(nums):
#     a = 0
    
#     for i in nums:
#         xor = a ^ i
#         print(f"xor: {xor}")
#         a = xor
    
#     return a


print(findSingleNumber([1])) # expected: 1
print(findSingleNumber([2,2,1])) # expected: 1
print(findSingleNumber([4,1,2,1,2])) # expected: 4
print(findSingleNumber([0,3,1,4,2,3,1,2,4])) # expected: 0



"""
Exercise 2: "1. Two Sum" (https://leetcode.com/problems/two-sum/)

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

* Notes:
- You may assume that each input would have exactly one solution, and you may not use the same element twice.
- You can return the answer in any order.

* Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

def twoSum(nums, target):
    prev_nums = {}

    for index in range(len(nums)):
        first_num = nums[index]
        second_num = target - first_num

        if second_num in prev_nums:
            index2 = prev_nums[second_num]
            return [index2, index]
        else:
            prev_nums[first_num] = index 

    # simply return None if no two sum
    return None


print(twoSum([3], 3))
print(twoSum([1,2,3], 3))
print(twoSum([1,1], 3))
print(twoSum([1,9,4,23,16,43], 53))
print(twoSum([1,4,8,9,3], 13))