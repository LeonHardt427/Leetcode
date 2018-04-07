# -*- coding: utf-8 -*-
# @Time    : 2018/4/4 19:08
# @Author  : LeonHardt
# @File    : 3_Longest_Substring_Without_Repeating.py


"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        self.lens = 0
        words = []

        for word in self.s:
            if (word in words) is False:
                words.append(word)
                if len(words) > self.lens:
                    self.lens = len(words)
            else:
                while(word in words):
                    words.pop(0)
                words.append(word)
        if len(words) > self.lens:
            self.lens = len(words)
        return self.lens

b = Solution()
a = b.lengthOfLongestSubstring("aab")
print(a)

