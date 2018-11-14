# coding=utf-8
"""
Suzuki needs help lining up his students!

Today Suzuki will be interviewing his students to ensure they are progressing in their training.
He decided to schedule the interviews based on the length of the students name in descending order.
The students will line up and wait for their turn.

You will be given a string of student names. Sort them and return a list of names in descending order.
 lst = ['Takehiko',
        'Takayuki',
        'Takahiro',
        'Takeshi',
        'Takeshi',
        'Takashi',
        'Tadashi',
        'Takeo',
        'Takao']

Names of equal length will be returned in descending alphabetical order such that:
string = "xxa xxb xxc xxd xa xb xc xd"
Returns
['xxd', 'xxc', 'xxb', 'xxa', 'xd', 'xc', 'xb', 'xa']
"""


def lineup_students(string):
    """
    # solved by others
    """
    return sorted(sorted(string.split()), key=len)[::-1]


if __name__ == "__main__":
    s1 = "Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi Takeshi"
    print lineup_students(s1)

"""
def lineup_students(s):
    return sorted(s.split(), key=lambda i:(len(i),i), reverse=True)
"""