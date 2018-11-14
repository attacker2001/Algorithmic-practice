#!/usr/bin/env python
# coding=utf-8

"""
Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive
alphabetic characters and numeric digits that
occur more than once in the input string.
The input string can be assumed to contain only alphanumeric characters,
including digits, uppercase and lowercase alphabets.

Example

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabbcdeB" -> 2 # 'a' and 'b'
"indivisibility" -> 1 # 'i'
"Indivisibilities" -> 2 # 'i' and 's'
"aa11" -> 2 # 'a' and '1'
"""


def duplicate_count(text):
    repeat_char = []
    count = 0
    for i in text.lower():
        if len(text) - len(text.replace(i, '')) >= 2\
                and (i not in repeat_char):
            repeat_char.append(i)
            count += 1
    return count


if __name__ == '__main__':
    print duplicate_count("abcddddd")
    # print bin_to_hex("1111")

"""
Solution 1:
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])

"""