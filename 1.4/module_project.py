

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



"""
Exercise 7

Given a binary string (ASCII encoded), write a function that returns the equivalent decoded text.

Every eight bits in the binary string represents one character on the ASCII table.

* Examples:
    csBinaryToASCII("011011000110000101101101011000100110010001100001") -> "lambda"
    01101100 -> 108 -> "l"
    01100001 -> 97 -> "a"
    01101101 -> 109 -> "m"
    01100010 -> 98 -> "b"
    01100100 -> 100 -> "d"
    01100001 -> 97 -> "a"
    csBinaryToASCII("") -> ""

* Notes:
    - The input string will always be a valid binary string.
    - Characters can be in the range from "00000000" to "11111111" (inclusive).
    - In the case of an empty input string, your function should return an empty string.
"""

def csBinaryToASCII(input_string):
    result = ""
    temp = ""
    count = 0

    for char in input_string:
        temp += char
        count += 1

        if count == 8:
            ascii_dec = int(temp, base=2)
            result += chr(ascii_dec)

            temp = ""
            count = 0

    return result


long_bin = "010001100110100101110010011100110111010000101100001000000111001101101111011011000"\
    "1110110011001010010000001110100011010000110010100100000011100000111001001101111011000100"\
        "1101100011001010110110100101110001000000101010001101000011001010110111000101100001000"\
            "000111011101110010011010010111010001100101001000000111010001101000011001010010000"\
                "00110001101101111011001000110010100101110"

long_bin_2 = "01000101011110000111000001100101011100100110100101100101011011100110001101100101"\
    "00100000011010010111001100100000011101000110100001100101001000000110111001100001011011010"\
        "1100101001000000110010101110110011001010111001001111001011011110110111001100101001000"\
            "000110011101101001011101100110010101110011001000000111010001101111001000000111010"\
                "00110100001100101011010010111001000100000011011010110100101110011011101000110"\
                    "000101101011011001010111001100101110"

print(csBinaryToASCII(""))
print(csBinaryToASCII("011011000110000101101101011000100110010001100001"))
print(csBinaryToASCII("0100100001100101011011000110110001101111"))
print(csBinaryToASCII(long_bin))
print(csBinaryToASCII(long_bin_2))



"""
Exercise 8

Given a number, write a function that converts that number into a string that contains "raindrop sounds"
corresponding to certain potential factors. A factor is a number that evenly divides into another number, 
leaving no remainder. Simplest way to test if a number is a factor of another is to use the modulo operator.

* Here are the rules for csRaindrop. If the input number:
    - has 3 as a factor, add "Pling" to the result.
    - has 5 as a factor, add "Plang" to the result.
    - has 7 as a factor, add "Plong" to the result.
    - does not have any of 3, 5, or 7 as a factor, the result should be the digits of the input number.

* Examples:
    csRaindrops(28) -> "Plong"
    28 has 7 as a factor, but not 3 or 5.

    csRaindrops(30) -> "PlingPlang"
    30 has both 3 and 5 as factors, but not 7.

    csRaindrops(34) -> "34"
    34 is not factored by 3, 5, or 7.
"""

def csRaindrops(number):
    dict = {3:"Pling", 5:"Plang", 7:"Plong"}
    
    result = "".join([dict[divisor] for divisor in dict if number % divisor == 0])
    
    if result != "":
        return result
    else:
        return str(number)


print(csRaindrops(28))
print(csRaindrops(30))
print(csRaindrops(34))
print(csRaindrops(35))
print(csRaindrops(17))