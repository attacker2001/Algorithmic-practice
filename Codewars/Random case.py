# coding=utf-8
"""
Write a function that will randomly upper and lower characters in a string -
randomCase() (random_case() for Python).

A few examples:

randomCase("Lorem ipsum dolor sit amet, consectetur adipiscing elit") ==
           "lOReM ipSum DOloR SiT AmeT, cOnsEcTEtuR aDiPiSciNG eLIt"

randomCase("Donec eleifend cursus lobortis") == "DONeC ElEifEnD CuRsuS LoBoRTIs"

Note: this function will work within the basic ASCII character set to make this kata easier -
so no need to make the function multibyte safe.

"""
import random


# def random_case(x):
#     string = []
#     for i in x:
#         string.append(i)
#     for i in xrange(len(x)):
#         if random.randint(0, 1):
#             string[i] = string[i].upper()
#         else:
#             string[i] = string[i].lower()
#
#     return "".join(string)


def random_case(x):
    return "".join([random.choice([i.upper(), i.lower()]) for i in x])


if __name__ == "__main__":
    print random_case("Lorem ipsum dolor sit amet, consectetur adipiscing elit")

"""
import random

def random_case(x):
    return "".join([random.choice([c.lower(), c.upper()]) for c in x])
"""