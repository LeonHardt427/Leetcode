# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 9:40
# @Author  : LeonHardt
# @File    : 6_ZigZag Conversion.py

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        self.s = s
        self.row = numRows
        if numRows == 1:
            return self.s
        else:
            array = []

            for temp in range(numRows):
                array.append([])
            for index, word in enumerate(s):
                numindex = index % (2*numRows-2)
                if numindex < numRows:
                    array[numindex].append(word)
                else:
                    array[(2*numRows-2) - numindex].append(word)
        summary = []
        for temp in range(numRows):
            if temp == 0:
                summary = array[0]
            else:
                summary = summary + array[temp]
        words = "".join(summary)
        return words


if __name__ == '__main__':
    a = Solution()
    print(a.convert("PAYPALISHIRING", 3))



