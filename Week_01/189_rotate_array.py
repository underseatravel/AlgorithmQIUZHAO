#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 16:39
# @Author  : weiyu
# @File    : 189_rotate_array.py


# 三次翻转
class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - k -1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)


    def reverse(self,nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1


# 切片
# class Solution:
#     def rotate(self, nums, k):
#         n = len(nums)
#         nums[:] = nums[n - k:] + nums[:n - k]


# 插入
# class Solution:
#     def rotate(self, nums, k):
#         for _ in range(k):
#             nums.insert(0, nums.pop())