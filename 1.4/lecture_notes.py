
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