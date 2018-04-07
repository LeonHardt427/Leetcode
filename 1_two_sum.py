# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 21:57
# @Author  : LeonHardt
# @File    : 1_two_sum.py



"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target

        max_index = len(self.nums)
        for index in range(max_index):
            for index_2 in range(index, max_index):
                if nums[index] + nums[index_2] == self.target:
                    return [index, index_2]









