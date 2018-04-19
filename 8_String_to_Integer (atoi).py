# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 20:50
# @Author  : LeonHardt
# @File    : 8_String_to_Integer (atoi).py


"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

"""


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        self.str = str
        temp = ""
        try:
            temp_list = self.str.split(" ")
            flag = 0
            for i in range(len(temp_list)):
                temp = temp_list[i]
                if temp != "":
                    flag = 1
                    break
            if flag == 0:
                temp = 0
        except ValueError:
            temp = self.str

        try:
            temp = float(temp)
            if temp != float("inf") and temp != float("-inf"):
                temp = int(temp)
        except ValueError:
            temp = 0
        finally:
            if temp > 2147483647 or temp == float("inf"):
                temp = 2147483647
            elif temp < -2147483647 or temp ==float("-inf"):
                temp = -2147483647

        return temp


if __name__ == '__main__':
    a = Solution()
    print(a.myAtoi('+11e530408314'))

