
"""
# Sprint 1 Module 2 - Problem Solving

The U.P.E.R. Framework:

(U)nderstand
    - know what youre being asked to do
    - create 3-5 test-cases, you can actually discover the optimal algorithm in doing so
        - tests should not be too easy or too hard

(P)lan
    - takes the most time for this step
    - you know the problem, whats the game plan?
    - address each of the cases you developed in the Understand step
    - what patterns have you seen before that you can apply?
    - what techniques/data structures can I use?
    - start with brute force if no immediate optimal solution
    - rough layout of code
    - what functions do I need?
    - DO NOT PROCEED TO NEXT STEP if you don't know what you'll be coding

(E)xecute
    - convert your pseudocode into actual code
    - code your algorithm
    - if you plan properly this should be the fastest step yet
    - pay attention to any bugs

(R)eflect
    - correct any bugs
        - make a note of the bug but don't immediately address
        - make sure to take time to and plan how to fix
            - DO NOT do anything rash and regress your code
    - go through line by line and explain the solution
    - test your code with your test cases from step 1
    - state your runtime and space complexity if you havent addressed in plan step

"""




"""
Exercise 1: Number of Good Pairs (https://leetcode.com/problems/number-of-good-pairs/)

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
"""

def numIdenticalPairs(nums):
        dict = {}

        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        max_pairs = 0

        # Lets say we have a value repeated 4 times.
        # Since we're looking at pairs, its like having 2 sets for each count, i.e. count^2
        # But the value cannot be paired with itself, so only count-1 max
        # Finally divide by 2 to get the number of pairs

        # Since the value can only be a pair with everything but itself, it would look like:
        # ((count^2 - count) / 2)

        for count in dict.values():
            max_pairs += ((count**2) - count) / 2

        return int(max_pairs)




"""
Exercise 2: Richest Customer Wealth (https://leetcode.com/problems/richest-customer-wealth/)

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
"""