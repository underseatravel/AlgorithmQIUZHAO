#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 22:24
# @Author  : weiyu
# @File    : 77_combinations.py

# 递归 加 剪枝
class Solution:
    def combine(self, n, k):
        res = []
        nums = range(1, n + 1)
        self.recursion(nums, k, 0, [], res)
        return res

    def recursion(self, nums, k, index, s, res):
        if k == 0:
            res.append(s)
        if k > len(nums) - index + 1:
            return
        for i in range(index, len(nums)):
            self.recursion(nums, k - 1, i + 1, s + [nums[i]], res)
