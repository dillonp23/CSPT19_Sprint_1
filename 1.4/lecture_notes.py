
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