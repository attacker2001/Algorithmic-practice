#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 17. Letter Combinations of a Phone Number.py 
@time: 2019/05/04


Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want
"""


class Solution:
    def letterCombinations(self, digits: str) -> list:
        tel_key = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        if len(digits) == 1:
            return list(tel_key[digits])
        elif len(digits) == 0:
            return []
        else:
            result = list(tel_key[digits[0]])
            for digit in digits[1:]:
                tmp = []
                for i in result:
                    for j in list(tel_key[digit]):
                        tmp.append(i + j)
                result = tmp.copy()

        return list(set(result))


if __name__ == '__main__':
    a = Solution()
    print(a.letterCombinations(""))
    print(a.letterCombinations("23"))
    print(sorted(a.letterCombinations("234")) == ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", "bdg",
                                                  "bdh",
                                                  "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi", "cdg", "cdh", "cdi",
                                                  "ceg",
                                                  "ceh", "cei", "cfg", "cfh", "cfi"])

"""
Other solutions:
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        self.dict = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs","8":"tuv","9":"wxyz","10":" "}
        result = [""]
        for digit in digits:
            lst = self.dict[digit]
            newresult = []
            for char in lst:
                for str in result:
                    newresult.append(str+char)
            result = newresult
        return result
        

class Solution:
    def letterCombinations(self, digits: str) -> list:
        tel_key = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        if len(digits) == 1:
            return list(tel_key[digits])
        elif len(digits) == 0:
            return []
        else:
            result = list(tel_key[digits[0]])
            for digit in digits[1:]:
                tmp = []
                for i in result:
                    for j in list(tel_key[digit]):
                        tmp.append(i + j)
                result = tmp.copy()

        return result

"""