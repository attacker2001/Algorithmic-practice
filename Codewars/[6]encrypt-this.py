#!/usr/bin/env python  
# coding:utf-8 
""" 
@author: attacker2001 
@file: [6]encrypt-this.py 
@time: 2018/11/26
@project: Algorithm-Exercise 
@software: PyCharm
"""

"""
https://www.codewars.com/kata/encrypt-this/train/python

Acknowledgments:
I thank yvonne-liu for the idea and for the example tests :)

Description:
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:

    The first letter needs to be converted to its ASCII code.
    The second letter needs to be switched with the last letter

Keepin' it simple: There are no special characters in input.
Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
"""


def encrypt_this(text):
    temp = ""

    if text:
        word_list = text.split(' ')
        for word in word_list:
            if len(word) > 2:
                temp += (str(ord(word[0])) + word[-1] + word[2:-1] + word[1] + ' ')
            elif len(word) == 2:
                temp += (str(ord(word[0])) + word[1] + ' ')
            elif len(word) == 1:
                temp += (str(ord(word)) + ' ')
            else:
                pass

    return temp.strip()


if __name__ == '__main__':

    print encrypt_this("") == ""
    print encrypt_this("A wise old owl lived in an oak") == "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"
    print encrypt_this("The more he saw the less he spoke") == "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"
    print encrypt_this("The less he spoke the more he heard") == "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"
    print encrypt_this(
        "Why can we not all be like that wise old bird") == "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"
    print encrypt_this("Thank you Piotr for all your help") == "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"



"""
Other solutions:

(1)
def swapper(w):
    return w if len(w)<2 else w[-1] + w[1:-1] + w[0]

def encrypt_this(s):
    return ' '.join(w if not w else str(ord(w[0])) + swapper(w[1:]) for w in s.split())

# 我认为好的解法应该是“即使一个人没有看过题目，但是通过阅读代码就能反过去推测出题目的解法”
# 因此个人认为这个解法只是最精简的写法，并不适用于实际的工程项目。


(2)
def encrypt_this(text):
    result = []
    
    for word in text.split():
        # turn word into a list
        word = list(word)
        
        # replace first letter with ascii code
        word[0] = str(ord(word[0]))
        
        # switch 2nd and last letters
        if len(word) > 2:
            word[1], word[-1] = word[-1], word[1]
        
        # add to results
        result.append(''.join(word))
    
    return ' '.join(result)

(3)
def encrypt_word(word):
    result = list(word)
    result[0] = str(ord(result[0]))
    if len(word) > 1:
        result[1], result[-1] = result[-1], result[1]
    return "".join(result)
    
def encrypt_this(text):
    return " ".join(encrypt_word(word) for word in text.split())

"""
