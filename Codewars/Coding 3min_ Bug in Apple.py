# coding=utf-8

"""
This is the simple version of Shortest Code series. If you need some challenges, please try the challenge version.

    Task:

    Find out "B"(Bug) in a lot of "A"(Apple).

    There will always be one bug in apple, not need to consider the situation that without bug or more than one bugs.

    input: string Array apple

    output: Location of "B", [x,y]

Series:
    Bug in Apple
    Father and Son
    Give me the equation
    Collatz Array(Split or merge)
    Trypophobia
    Virus in Apple
    Balance Attraction
    Tidy up the room
    Symmetric Sort
    Are they symmetrical?
    Waiting for a Bus
"""


# def sc(apple):
#     rows = 0
#     for i in apple:
#         if 'B' in i:
#             return [rows, i.index('B')]
#         rows += 1

# def sc(apple):
#     for i in enumerate(apple):
#         if 'B' in i[1]:
#             return [i[0], i[1].index('B')]

# def sc(apple):
#     return [[i[0], i[1].index('B')] for i in enumerate(apple) if 'B' in i[1]][0]

def sc(apple):
    return [[x, y.index('B')] for x, y in enumerate(apple) if 'B' in y][0]


if __name__ == "__main__":
    a = [
        ["A","A","A","A","A"],
        ["A","A","A","A","A"],
        ["A","A","A","A","A"],
        ["A","A","B","A","A"],
        ["A","A","A","A","A"]
        ]
    print sc(a)

"""
def sc(apple):
    return [[x,y.index("B")] for x,y in enumerate(apple) if "B" in y][0]
"""