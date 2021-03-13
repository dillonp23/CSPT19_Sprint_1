
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
Exercise 1: "1512. Number of Good Pairs" (https://leetcode.com/problems/number-of-good-pairs/)

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

** Example **
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


print(numIdenticalPairs([1,2,3,1,1,3])) # expected: 4
print(numIdenticalPairs([1,1,1,1])) # expected: 6
print(numIdenticalPairs([1,2,3])) # expected: 0



"""
Exercise 2: "1672. Richest Customer Wealth" (https://leetcode.com/problems/richest-customer-wealth/)

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer 
has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is 
the customer that has the maximum wealth.

** Example **
    Input: accounts = [[1,2,3],[3,2,1]]
    Output: 6
    Explanation:
    1st customer has wealth = 1 + 2 + 3 = 6
    2nd customer has wealth = 3 + 2 + 1 = 6
    Both customers are considered the richest with a wealth of 6 each, so return 6.

    Constraints:
        m == accounts.length
        n == accounts[i].length
        1 <= m, n <= 50
        1 <= accounts[i][j] <= 100


* Understand:
    - input is an array of customers, where each customer is represented by an array of bank accounts
    - for each customer get the sum of their bank accounts
    - return an int represting the amount of money that is in the wealthiest account

* Plan:
    def max_wealth_function(input_list):
        # store a max_wealth variable w/ init = 0

            # loop through the outer accounts array
                # cust_accounts = accounts[index]

                # loop through accounts and get sum

                # if sum is > max, update max

            # return max
"""

# Brute Force Solution:
# def maximumWealth(accounts):
#     max_wealth = 0

#     for index in range(len(accounts)):
#         customer_accounts = accounts[index]
#         wealth = 0

#         for item in customer_accounts:
#             wealth += item
        
#         if wealth > max_wealth:
#             max_wealth = wealth

#     return max_wealth


# Optimized Solution:
# def maximumWealth(accounts):
#     max_wealth = 0

#     for index in range(len(accounts)):
#         customer_wealth = sum(accounts[index])
#         max_wealth = max(customer_wealth, max_wealth)

#     return max_wealth


# Fully Reduced Solution:
def maximumWealth(accounts):
    return max(map(sum, accounts))


print(maximumWealth([[1,2,3],[3,2,1]])) # => expected: 6
print(maximumWealth([[1,2,3],[4,5,6]])) # => expected: 15
print(maximumWealth([[1,2],[0,0],[5,6]])) # => expected: 11
print(maximumWealth([[1,2,3]])) # => expected: 6



"""
Exercise 3: "961. N-Repeated Element in Size 2N Array" (https://leetcode.com/problems/n-repeated-element-in-size-2n-array/)

In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.


** Example **
    Input: [1,2,3,3]
    Output: 3
"""

def repeatedNTimes(nums):
    # Given a list of nums, length of list is 2N, w/ N+1 unique elements, and one element (x) repeats N times
    # length of list / 2 == the number of times (N) that the element (x) is repeated

    n = len(nums) / 2

    # we want to return the value (x) that is repeated N times
    # use a dictionary with "x" as key and "count" as the value
    dict = {}

    for x in nums:
        # if "x" in dict, increment, otherwise set dict[x] = 1
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
    
        # if the "count" == "n" then we'll return the key "x"
        count = dict[x]

        if count == n:
            return x

print(repeatedNTimes([1,2,3,3])) # expected: 3
print(repeatedNTimes([2,1,2,5,3,2])) # expected: 2
print(repeatedNTimes([5,1,5,2,5,3,5,4])) # expected: 5