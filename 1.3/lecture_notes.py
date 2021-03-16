
"""
Sprint 1 Module 3: Time & Space Complexity

* Least Time/Space *
- O(1): Constant
- O(log n): Logarithmic - moves towards constant as input size grows
- O(n): Linear - increases proportionally to input size
- O(n log n)
- O(n^2): Quadratic 
- O(c^n): Exponential - increases exponentially as input size increases
- O(n!): Factorial
* Most Time/Space *

"""



"""
Exercise 1: "136. Single Number" (https://leetcode.com/problems/single-number/)

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

* Example:
    Input: nums = [2,2,1]
    Output: 1
"""



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