# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 19:41
# @Author  : LeonHardt
# @File    : 10_Regular Expression Matching.py

"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

"""
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.str = s
        self.pat = p

        words_s = []
        words_p = []
        temp = 0
        for word in self.str:
            if word != temp:
                words_s.append(word)
            temp = word
        for word_p in self.pat:
            words_p.append(word_p)

        while words_p != []:
            temp = words_p[-1]
            if temp != words_s[-1] and temp != '.' and temp != '*':
                return False
            elif temp == words_s[-1] or temp == '.':
                words_s.pop()
                words_p.pop()
            elif temp == '*':
                words_p.pop()
                if words_s[-1] != words_p[-1] and words_p[-1] != '.':
                    words_p.pop()
                elif words_s[-1] == words_p[-1] and words_p[-1] != '.':
                    words_p.pop()
                    words_s.pop()
                # elif words_p[-1] != '.':

        if words_s == []:
            return True
        else:
            return False


if __name__ == '__main__':
    a =Solution()
    print(a.isMatch("asssdf", ""))










