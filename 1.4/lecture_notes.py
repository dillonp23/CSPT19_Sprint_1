
"""
# Sprint 1 Module 4 - RAM & Data Structures in Memory


* Numbers can be represented in base 2 or base 10
    - base 2 => binary
    - base 10 => decimal


* "Binary" (base 2)
    - a binary digit is a bit
    - 8 bits in a byte
    - computers are made up of transistors
    - each transistor is a state of "on" (1/true) or "off" (0/false)


* Two main character encodings:
    1. ASCII
    - 2^7 or 128 characters

    2. Unicode 
    - 2^21 characters = ~2.1 million characters


Media types in computers:
    * Images
        - made up of pixels, which are just combinations of RGB colors represented as numbers

    * Video
        - similar to images just more data

    * Audio
        - converts waveforms sampled at different rates to a number frequency
            - 8-bit or 16-bit
        
    * Code in binary (https://indianpythonista.wordpress.com/2018/01/04/how-python-runs/)
        - an "Interpreter" converts high level language to low level code
        - "Compiler" => translates .py code to byte code
        - "Virtual Machine" => translates the byte code to machine code that can be executed by the CPU
"""


"""
Exercise:

1. convert the following from binary to decimal
    10010 => 18
    11000 => 24

2. convert from decimal to binary:
    53 => 110101
    15 => 1111
    17 => 10001
    20 => 10100
    27 => 11011


* The max number n binary digits can represent is (2^n-1)
"""


"""
Primary components of computer relevant to us:

1. CPU
    - executes instructions
    - the comp brain

2. RAM
    - random access memory
    - temporary, fast
    - 12*GB (128 * 10^9 bytes) of RAM in iMac Pro

    - the working "scratchpad" of computer
    - used to store code and data being actively used
    - 

3. Persistent Storage
    - long term storage (SSD, HD)
    - 2TB (2 x 10^12 bytes) of storage in an iMac Pro


Numbers & Memory in Computers:
- fixed-width integers
    - i.e. no matter how large the value, each integer takes up same amount of space

- computers typically use 32 bit or 64 bit
- since they are fixed width:
    - constant space
    - operations are in constant time

* if we reach the maximum number that a computer can represent what happens?
    - number overflow!


Arrays & Memory:
    - RAM similar to an array/list
    - each slot has fixed size
    - fast indexing


Strings & Memory:
- a list of individual characters
- either ASCII or Unicode

If we wanted to store a string with a length of 5 in memory that has 32-bit slots, 
then each character would consist of 32-bits.
So it would take a total of 160 bits to store the string (160 bits = 20 bytes).
"""



"""
Exercise 1: "709. To Lower Case" (https://leetcode.com/problems/to-lower-case/)

Implement function toLowerCase() that has a string parameter str, and returns the same string in lowercase,
without using the built in lower() function.

* Examples:
    "Hello" => "hello"
    "HELLO" => "hello"
    "h3l8L0" => "h3l8l0"
    "hello" => "hello"

* Hints:
    ord(x) gets the encoding value of character
    chr(x) converts letter to encoding value
    lowercase equiv of upper case is charcater encoding +32
"""

def toLowerCase(input_str):
    result = ""

    for x in input_str:
        num = ord(x)

        if 65 <= num <=90:
            num += 32
            result += chr(num)
        else:
            result += x
        
    return result


print(toLowerCase("Hello"))
print(toLowerCase("HELLO"))
print(toLowerCase("hello"))
print(toLowerCase("h3l8L0"))



"""
Exercise 2: "191. Number of 1 Bits" (https://leetcode.com/problems/number-of-1-bits/)

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

* Notes:
In some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a 
signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, 
whether it is signed or unsigned. In Java, the compiler represents the signed integers using 2's complement notation. 
Therefore, in Example 3, the input represents the signed integer -3.
 

* Examples:
    Input: n = 00000000000000000000000000001011
    Output: 3
    Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

    Input: n = 00000000000000000000000010000000
    Output: 1
    Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

    Input: n = 11111111111111111111111111111101
    Output: 31
    Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 
* Constraints:
    The input must be a binary string of length 32.

"""

def numberOfOneBits(n: int):
    return bin(n).count('1')


print(numberOfOneBits(0o00000000000000000000000000001011))
print(numberOfOneBits(0o00000000000000000000000010000000))
print(numberOfOneBits(0o11111111111111111111111111111101))
print(numberOfOneBits(0o00000000000110000001111111100010))


# import sys

# def numberOfOneBits(n: int):
#     orig_len = len(str(n))
#     n = int(n)
#     orig_size = sys.getsizeof(n)

#     s = bin(n)
#     prestrip = len(s)
#     pre_size = sys.getsizeof(s)

#     s_new = s.lstrip('-0b')
#     poststrip = len(s_new)
#     post_size = sys.getsizeof(s_new)

#     print(f"Original length of input: {orig_len} \
#         \n orig_size: {orig_size}\
#         \n s_orig: {s}\
#         \n prestrip length: {prestrip}\
#         \n pre_size: {pre_size}\
#         \n s_new: {s_new}\
#         \n poststrip length: {poststrip}\
#         \n post_size: {post_size}")

# def numberOfOneBits(n):
#     orig_size = sys.getsizeof(n)
#     orig_info = sys.int_info

#     s = bin(n)
#     count = s.count('1')
#     s_size = sys.getsizeof(s)

#     print(f"orig_size: {orig_size}\
#         \n orig_info: {orig_info}\
#         \n s: {s}\
#         \n count: {count}\
#         \n s_size: {s_size}")