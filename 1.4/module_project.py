

# Sprint 1 - Module 4 Project

"""
Exercise 3: 

Convert 78 to binary, then add the resulting digits in decimal

78 -> binary -> sum of digits

Answer: 78 -> 1001110 -> sum: 1+1+1+1 = 4
"""


"""
Exercise 5:

In order to store strings, computers encode with ASCII or Unicode. In ASCII, each character can be represented
by 7 bits (although commonly stored as 8 bits). With this knowledge, what is the maximum number of characters
possible in an ASCII set?

Answer: each bit can be either a one or zero, therefore ASCII representation with 7 bits would be:
        2^7 = 128 charcaters
"""


"""
Exercise 6

Given an integer, write a function that reverses the bits (in binary) and returns the integer result.

* Notes:
    The input integer will not be negative.

* Examples:
    csReverseIntegerBits(417) -> 267
    417 in binary is 110100001. Reversing the binary is 100001011, which is 267 in decimal.
    csReverseIntegerBits(267) -> 417
    csReverseIntegerBits(0) -> 0
"""

def csReverseIntegerBits(n):
    # convert int to binary string
    num_string = bin(n)

    # strip prefix, reverse
    num_string = num_string[2:][::-1]

    # add prefix, convert to int(n, base=2)
    return int(f"0b{num_string}", base=2)


print(csReverseIntegerBits(417))
print(csReverseIntegerBits(267))
print(csReverseIntegerBits(2017))
print(csReverseIntegerBits(1087))
print(csReverseIntegerBits(0))