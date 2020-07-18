#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 17:31
# @Author  : weiyu
# @File    : 21_merge_two_sorted_lists.py


# 递归
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val: l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

# 迭代
# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         dummy = cur = ListNode(0)
#         while l1 and l2:
#             if l1.val < l2.val:
#                 cur.next = l1
#                 l1 = l1.next
#             else:
#                 cur.next = l2
#                 l2 = l2.next
#             cur = cur.next
#         cur.next = l1 or l2
#         return dummy.next