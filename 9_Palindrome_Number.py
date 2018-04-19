# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 19:16
# @Author  : LeonHardt
# @File    : 9_Palindrome_Number.py


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        self.num = x
        count = []
        if self.num == 0:
            return True
        elif self.num < 0:
            return False
        else:
            while self.num != 0:
                count.append(self.num % 10)
                self.num = int(self.num / 10)
            print(count)
            for i in range(len(count)):
                if count[i] != count[-(i+1)]:
                    return False
            return True


if __name__ == '__main__':
    a = Solution()
    print(a.isPalindrome(1))
