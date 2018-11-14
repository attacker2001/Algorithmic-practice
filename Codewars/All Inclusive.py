# coding=utf-8
"""
input:

    a string strng
    an array of strings arr

Output of function contain_all_rots(strng, arr) (or containAllRots or contain-all-rots):

    a boolean true if all rotations of strng are included in arr
    false otherwise

Examples:

contain_all_rots(
  "bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]) -> true

contain_all_rots(
  "Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl", "ipywee"]) -> false)
"""


def contain_all_rots(strng, arr):
    for i in xrange(len(strng)):
        strng = strng[1:] + strng[0:1]
        if strng not in arr:
            return False
    return True


if __name__ == '__main__':
    print contain_all_rots("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"])
    print contain_all_rots("Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl", "ipywee"])


"""
题目要求:
    判断所有的字符串(包括回旋)是否都在数组中
核心技术:
    实现字符串的回旋:
    for i in xrange(len(strng)):
        strng = strng[1:] + strng[0:1]
"""
