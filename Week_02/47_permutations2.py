#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 23:51
# @Author  : weiyu
# @File    : 47_permutations2.py


class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        self.recursion(nums, [], res)
        return res

    def recursion(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.recursion(nums[:i] + nums[i + 1:], path + [nums[i]], res)