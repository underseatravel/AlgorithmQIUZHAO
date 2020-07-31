#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 17:02
# @Author  : weiyu
# @File    : 78_subsets.py

# 迭代
class Solution:
    def subsets(self, nums):
        res = [[]]
        for num in nums:
            res = res + [[num] + sub for sub in res]
        return res


# 递归
class Solution:
    def subsets(self, nums):
        res = []
        self.recursion(0, nums, [], res)
        return res

    def recursion(self, i, nums, tmp, res):
        res.append(tmp)
        for j in range(i, len(nums)):
            self.recursion(j + 1, nums, tmp + [nums[j]], res)



