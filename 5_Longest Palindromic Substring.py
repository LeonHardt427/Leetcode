# -*- coding: utf-8 -*-
# @Time    : 2018/4/7 14:49
# @Author  : LeonHardt
# @File    : 5_Longest Palindromic Substring.py

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.


Example:

Input: "cbbd"

Output: "bb"

思路：从最大长度的字符串逐渐缩小，找到回文为止

"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.lis = s
        total = len(self.lis)
        if total == 1:
            return self.lis
        leng = range(1, total+1)
        for length in reversed(leng):
            for start_num in range(0, total-length+1):
                s_temp = self.lis[start_num : start_num + length]
                flag = 0
                for i in range(length):
                    if s_temp[i] != s_temp[-i - 1]:
                        flag += 1
                if flag == 0:
                    return s_temp
                else:
                    flag = 0

        return self.lis[0]

if __name__ == '__main__':
    a = Solution()
    c = a.longestPalindrome("sdssdsdsfsfasdfasfdasdfadf")
    print(c)