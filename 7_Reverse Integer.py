# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 10:13
# @Author  : LeonHardt
# @File    : 7_Reverse Integer.py

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        self.num = x
        temp = []
        flag = 0
        if self.num < 0:
            flag = 1
            self.num = 0 - self.num

        if self.num >= (2**31):
            return 0
        else:
            temp_num = self.num
            while(temp_num):
                temp.append(temp_num % 10)
                temp_num = int(temp_num / 10)
            temp.reverse()
            result = 0
            for index, i in enumerate(temp):
                if index == 0:
                    result = i
                else:
                    result = result + i*(10**index)

            if result >= (2 ** 31):
                return 0

            elif flag == 1:
                result = 0 - result
            return result


if __name__ == '__main__':
    a = Solution()
    print(a.reverse(1534236469))


