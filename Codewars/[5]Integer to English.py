# coding=utf-8

"""
For a given positive integer convert it into its English representation.
All words are lower case and are separated with one space. No trailing spaces are allowed.

To keep it simple, hyphens and the writing of the word 'and' both aren't enforced.
 (But if you are looking for some extra challenge, such an output will pass the tests.)

Large number reference: http://en.wikipedia.org/wiki/Names_of_large_numbers (U.S., Canada and modern British)

Input range: 1 -> 10**26 (10**16 for JS)

Examples:

int_to_english(1) == 'one'

int_to_english(10) == 'ten'

int_to_english(25161045656) == 'twenty five billion one hundred sixty one million forty five thousand
six hundred fifty six'

or

int_to_english(25161045656) == 'twenty five billion one hundred sixty-one million forty-five thousand
six hundred and fifty-six'
"""


def int_to_english(n):
    new_num = ''
    count = 0
    for i in str(n)[::-1]:
        new_num += i
        count += 1
        if count % 3 == 0:
            new_num += ','
    new_num = new_num[::-1]

    one_to_ten = 'one two three four five six seven eight nine ten'.split(' ')
    eleven_to_twenty = 'eleven twelve thirteen fourteen fifteen sisteen seventeen eighteen nineteen'.split(' ')
    twenty_to_ninty = 'twenty thirty forty fifty sixty seventy eighty ninety'.split(' ')
    # print one_to_ten, eleven_to_twenty, twenty_to_ninty
    for i in new_num.split(',')[::-1]:
        print int(i)
        if int(i) <= 10:
            print one_to_ten[i]


if __name__ == '__main__':
    int_to_english(123006)
