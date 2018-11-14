# coding=utf-8

"""
Get All Possible Anagrams from a Hash

Given a hash of letters and the number of times they occur,
 recreate all of the possible anagram combinations that could be
  created using all of the letters, sorted alphabetically.

The inputs will never include numbers, spaces or any special characters,
 only lowercase letters a-z.

E.g. get_words({2=>["a"], 1=>["b", "c"]}) =>
["aabc", "aacb", "abac", "abca", "acab", "acba",
"baac", "baca", "bcaa", "caab", "caba", "cbaa"]

"""


from itertools import permutations


def get_words(hash_of_letters):
    word = ''
    for number, letters in hash_of_letters.iteritems():
        for letter in letters:
            word += number*letter
    print word
    return sorted([''.join(x) for x in set(permutations(word))])

if __name__ == "__main__":
    print get_words({1: ['g', 'e'], 2: ['h'], 3: ['a']})


"""
from itertools import permutations

def get_words(hash_of_letters):
    word=[]
    for value,characters in hash_of_letters.iteritems():
        for character in characters:
            word.append(character*value)
    return sorted(set([''.join(w) for w in permutations(''.join(word))]))
"""