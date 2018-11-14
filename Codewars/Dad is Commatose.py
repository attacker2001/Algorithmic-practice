# coding = UTF-8

'''
Your dad doesn't really get punctuation, and he's always putting extra commas in when he posts. You can tolerate the run-on sentences, as he does actually talk like that, but those extra commas have to go!

Write a function called dadFilter that takes a string as argument and returns a string with the extraneous commas removed. The returned string should not end with a comma or any trailing whitespace.

'''

# def dad_filter(string):
#     temp = list(string.strip()); string = temp[:]
#     cnt = 0
#     for i in xrange(1, len(temp)):
#         if temp[i] == temp[i-1] == ',':
#             string.pop(i - cnt)
#             cnt += 1
#     if string[-1] == ',':
#         string.pop(len(string)-1)
#     return ''.join(string)
import re

def dad_filter(string):
    string = re.sub(r',+', ',', string.strip())

    if string[-1] == ',':
        return string[:-1]
    else:
        return string




def main():
    s = "Luke,,,,,,,,, I am your father,,,,,,,,,  "
    print dad_filter(s)



if __name__ == '__main__':
    main()

'''
Other Solution:
def dad_filter(string):
    return ",".join([w for w in string.rstrip(", ").split(",") if w != ""])

'''