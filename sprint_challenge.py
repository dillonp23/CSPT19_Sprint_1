
# Sprint 1 - Final Assessment

"""
Exercise 1

Given a string (the input will be in the form of an array of characters), write a function that returns the reverse of the given string.

* Examples:
    csReverseString(["l", "a", "m", "b", "d", "a"]) -> ["a", "d", "b", "m", "a", "l"]
    csReverseString(["I", "'", "m", " ", "a", "w", "e", "s", "o", "m", "e"]) -> ["e", "m", "o", "s", "e", "w", "a", " ", "m", "'", "I"]

* Notes:
    - Your solution should be "in-place" with O(1) space complexity. Although many in-place functions do not return the modified 
    input, in this case you should.
    - You should try using a "two-pointers approach".
    - Avoid using any built-in reverse methods in the language you are using (the goal of this challenge is for you to 
    implement your own method).
"""

def csReverseString(chars):
    last_index = len(chars) - 1
    
    for i in range(int(len(chars)/2)):
        temp = chars[i]
        chars[i] = chars[last_index]
        chars[last_index] = temp

        last_index -= 1


    return chars


print(csReverseString([]))
print(csReverseString(["a"]))
print(csReverseString(["a", "b"]))
print(csReverseString(["a", "b", "c"]))
print(csReverseString(["a", "b", "c", "d", "e"]))



"""
Summary & Explanation for Exercise 1:

I immediately knew how to go about this by using list slicing, but realized that wouldn't do as a solution since we were 
instructed not to use built in functionality. Obviously the  easiest solution would simply be "return chars[::-1]" however 
this is not acceptable in this circumstance. 

I planned to use the two pointers technique in order to iterate the list and at each index, swap the characters at opposite 
ends of the list. To do this I used  a temporary pointer to store the value for the first index, updated the value at the 
first index to the last index, and updated the last index with the temp variable. 

At first I was iterating the entire list and returning the list but this was giving the list back in the original order. 
I realized that I was swapping the indexes all the way through, so after getting past the first half of the array, doing 
the same swap method would return the list to its original state. I realized that I needed to only iterate up to the length 
of the list divided by 2, as stopping at the halfway mark is necessary to prevent reverting the list to the same order as the input.
"""




"""
Exercise 2

A palindrome is a word, phrase, number, or another sequence of characters that reads the same backward or forward. This includes 
capital letters, punctuation, and other special characters.

Given a string, write a function that checks if the input is a valid palindrome.

Examples:
    csCheckPalindrome("racecar") -> true
    csCheckPalindrome("anna") -> true
    csCheckPalindrome("12345") -> false
    csCheckPalindrome("12321") -> true

* Notes:
- Try to solve this challenge without using the reverse of the input string; use a for loop to iterate through the string and 
make the necessary comparisons.
- Something like the code below might be your first intuition, but can you figure out a way to use a for loop instead?

    def csCheckPalindrome(input_str):
        return input_str == "".join(reversed(input_str))
"""

def csCheckPalindrome(input_str):
    length = len(input_str)
    last_index = length - 1

    for i in range(int(length/2)):
        if input_str[i] != input_str[last_index]:
            return False
        
        last_index -= 1

    return True


print(csCheckPalindrome("racecar"))
print(csCheckPalindrome("anna"))
print(csCheckPalindrome("12345"))
print(csCheckPalindrome("12321"))
print(csCheckPalindrome("teststring"))




"""
Exercise 3

Given a string, write a function that removes all duplicate words from the input. The string that you return should 
only contain the first occurrence of each word in the string.

* Examples:
    csRemoveDuplicateWords("alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta") -> "alpha bravo golf delta"
    csRemoveDuplicateWords("my dog is my dog is super smart") -> "my dog is super smart"
"""

def csRemoveDuplicateWords(input_str):
    word_list = []
    word = ""
    length = len(input_str) - 1
    
    for i in range(len(input_str)):
        char = input_str[i]
        
        if char.isalpha():
            word += char
        
        if i == length or char == " ":
            if word not in word_list:
                word_list.append(word)
            
            word = ""         
    
    
    return " ".join(word_list)


print(csRemoveDuplicateWords("alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta"))
print(csRemoveDuplicateWords("my dog is my dog is super smart"))
print(csRemoveDuplicateWords("this is only a test string test"))



"""
Summary & Explanation for Exercise 3:

I ran into a few issues while solving this problem. I started out by trying to build a result string to return, 
but realized it was better to use a list and return that using the join method, using a single space as the separator. 
Doing so eliminated the need to add an additional space between words and kept things more straight forward for the algorithm.

One issue I ran into was not having the last word be added to the resulting string. To remediate this issue, I changed my 
for loop to iterate using the index rather than the character itself. By doing so, I was able to check if the character
was located at the last index of the string, and if so, would continue to check whether that word is in the resulting word 
list. By rewriting the algorithm in this way, I eliminated the need for a separate conditional statement after the for loop. 
This made the algorithm easier to understand and less verbose.


Time & Space Complexity for Exercise 3:

The time complexity for this solution is O(n) since we have to iterate through each character of the string. Off the top 
of my head, I can't think of a way to improve this.

The space complexity would be O(n) as well. We are creating a new list instance in order to store the words that appear 
in the input string. If the word is already in the list, then we continue to the next word. The space needed for the list 
to store the unique words will increase linearly as the input size increases. I suppose in some cases the space complexity 
could be between O(n) and O(1) depending on how many times the word appears in the input string, but generally speaking 
the space complexity will have to grow as the input size increases assuming that the input is not a string of many 
repetitive words.
"""