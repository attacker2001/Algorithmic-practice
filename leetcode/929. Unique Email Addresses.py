#!/usr/bin/env python  
# -*- coding: utf-8 -*-
""" 
@file: 929. Unique Email Addresses.py 
@time: 2019/05/04


Every email consists of a local name and a domain name, separated by the @ sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an email address,
 mail sent there will be forwarded to the same address without dots in the local name.
 For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
 (Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus sign will be ignored.
 This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.
  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.
How many different addresses actually receive mails?

Example 1:

Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails


Note:

1 <= emails[i].length <= 100
1 <= emails.length <= 100
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
"""


class Solution:
    def numUniqueEmails(self, emails: list) -> int:
        unique_emails = []
        for mail in emails:
            local_name, net_name = mail.split('@')[0], mail.split('@')[1]

            if '+' in local_name:
                local_name = local_name[:local_name.find('+')]
            if '.' in local_name:
                local_name = local_name.replace('.', "")

            if local_name + '@' + net_name not in unique_emails:
                unique_emails.append(local_name + '@' + net_name)
        return len(unique_emails)


if __name__ == '__main__':
    a = Solution()
    print(a.numUniqueEmails(
        ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))

"""
Other solutions:

class Solution(object):
    def numUniqueEmails(self, emails):
        actual = set()
        for email in  emails:
            local_name, net_name = email.split("@")[0].split("+")[0].replace(".", ""), email.split("@")[1]
            actual.add(local_name + "@" + net_name)
        return len(actual)

"""
