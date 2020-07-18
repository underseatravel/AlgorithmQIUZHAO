#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 18:27
# @Author  : weiyu
# @File    : 88_merge_sorted_array.py


# 双指针，从后往前
# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         while m > 0 and n > 0:
#             if nums1[m - 1] > nums2[n - 1]:
#                 nums1[m + n - 1] = nums1[m - 1]
#                 m -= 1
#             else:
#                 nums1[m + n - 1] = nums2[n - 1]
#                 n -= 1
#         if n > 0:
#             nums1[:n] = nums2[:n]


# 双指针，从前往后
class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1_copy = nums1[:m]
        nums1[:] = []
        p1 = p2 = 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]