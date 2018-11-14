# coding=utf-8

"""

Define two functions
hex_to_bin (hexToBin) and bin_to_hex (binToHex)

hex_to_bin

    Takes a hexadecimal string as an argument .

    Note:This string can contain upper or lower case characters and start with any amount of zeros.

    Returns the binary representation (without leading zeros) of the numerical value of the
hexadecimal string.

    Examples

    hex_to_bin("00F") -> "1111"
    hex_to_bin("5") -> "101"
    hex_to_bin("00000") -> "0"
    hex_to_bin('04D2') -> '10011010010'

bin_to_hex

    Takes a binary string (with or without leading zeros) as an argument .

    Returns the hexadecimal representation of the numerical value of the binary string.

        Note: Any none numerical characters should be lower case

    Examples

    bin_to_hex("1111") -> "f"
    bin_to_hex("000101") -> "5"
    bin_to_hex('10011010010') -> '4d2'

Note: You can assume all arguments are valid so there is no need for error checking.

Oh, and I've disabled a few things.

Any feedback would be much appreciated

"""
change_list = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
               '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12,
               'D': 13, 'E': 14, 'F': 15}


def hex_to_bin(hex_num):
    sum_dec = 0
    weight = 0
    for i in hex_num[::-1]:
        sum_dec += 16**weight * change_list[i]
        weight += 1
    print sum_dec


def bin_to_hex(bin_num):
    pass


if __name__ == '__main__':
    print hex_to_bin("00F")
    # print bin_to_hex("1111")

"""
Solution 1:
d = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

def chb(n, b1, b2, c=0, s=0, h=""):
    for i in list(reversed(n)):
        s+=d.index(i)*b1**c
        c+=1

    while s>0:
        s,h = s/b2, d[s%b2]+h

    return h if h else '0'

def bin_to_hex(b):
    return chb(b.lower(), 2, 16)

def hex_to_bin(b):
    return chb(b.lower(), 16, 2)


Solution 2:
TO_BIN = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
          '4': '0100', '5': '0101', '6': '0110', '7': '0111',
          '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
          'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}
TO_HEX = {v: k for k, v in TO_BIN.iteritems()}


def hex_to_bin(hex_string):
    return ''.join(TO_BIN[a] for a in hex_string.lower()).lstrip('0') or '0'
    # return '{:b}'.format(int(hex_string, 16))


def bin_to_hex(binary_string):
    length = len(binary_string)
    q, r = divmod(length, 4)
    if r > 0:
        length = 4 * (q + 1)
        binary_string = binary_string.zfill(length)
    return ''.join(TO_HEX[binary_string[a:a + 4]]
                   for a in range(0, length, 4)).lstrip('0') or '0'
    # return '{:x}'.format(int(binary_string, 2))

"""