# -*- coding: utf-8 -*-
# @Time    : 2018/4/3 9:45
# @Author  : LeonHardt
# @File    : 2_add_two_numbers.py


"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            carry = 0
            ret = ListNode(0)
            ret_Last = ret

        while(l1 or l2):
            sum = 0
            if(l1):
                sum = l1.val
                l1 = l1.next
            if (l2):
                sum += l2.val
                l2 = l2.next
            sum += carry
            ret_Last.next = ListNode(sum%10)
            ret_Last = ret_Last.next
            carry = (sum>=10)
        if (carry):
            ret_Last.next = ListNode(1)
        ret_Last = ret.next
        del ret
        return ret_Last
    