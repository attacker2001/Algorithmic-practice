# coding=utf-8
"""
Credit card issuer checking
Given a credit card number we can determine who the issuer/vendor is with a few basic knowns.

+============+=============+===============+
| Card Type  | Begins With | Number Length |
+============+=============+===============+
| AMEX       | 34 or 37    | 15            |
+------------+-------------+---------------+
| Discover   | 6011        | 16            |
+------------+-------------+---------------+
| Mastercard | 51-55       | 16            |
+------------+-------------+---------------+
| VISA       | 4           | 13 or 16      |
+------------+-------------+---------------+

Write a function (getIssuer(number) (get_issuer(number) for Python)) that will use the above known values
to determine the card issuer given a card number. If the number cannot be matched then the function should
return the string Unknown.

Some sample numbers and their issuer:

getIssuer(4111111111111111) == "VISA"
getIssuer(4111111111111) == "VISA"
getIssuer(4012888888881881) == "VISA"
getIssuer(378282246310005) == "AMEX"
getIssuer(6011111111111117) == "Discover"
getIssuer(5105105105105100) == "Mastercard"
getIssuer(5105105105105106) == "Mastercard"
getIssuer(9111111111111111) == "Unknown"

"""


def get_issuer(number):
    number = str(number)
    if len(number) not in [13, 15, 16]:
        return "Unknown"
    else:
        if number[0:2] in ['34', '37'] and len(number) == 15:
            return 'AMEX'

        elif number[0:4] == '6011' and len(number) == 16:
            return 'Discover'

        elif number[0:2] in [str(i) for i in list((range(51, 56)))] \
                and len(number) == 16:
            return 'Mastercard'

        elif number[0] == '4' and len(number) in [13, 16]:
            return 'VISA'

        else:
            return 'Unknown'

if __name__ == '__main__':
    print get_issuer(378282246310005)

"""
Other solution:
ISSUERS = {
    ((34, 37), (15,)): 'AMEX',
    ((6011,), (16,)): 'Discover',
    ((51, 52, 53, 54, 55), (16,)): 'Mastercard',
    ((4,), (13, 16)): 'VISA',
}

def get_issuer(number):
    return next((issuer for (starts, lengths), issuer in ISSUERS.items()
        if str(number).startswith(tuple(map(str, starts))) and len(str(number)) in lengths), 'Unknown')

"""
