# -*- coding: utf-8 -*-
# @Time    : 2018/4/7 13:46
# @Author  : LeonHardt
# @File    : 4_Median of Two Sorted Arrays.py

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""


def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    self.list = sorted((nums1 + nums2))

    size = len(self.list)
    if size % 2 == 0:
        return (self.list[int(size / 2)] + self.list[int((size / 2)) - 1]) / 2
    else:
        return self.list[int(size / 2)]

