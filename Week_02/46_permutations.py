#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 23:00
# @Author  : weiyu
# @File    : 46_permutations.py

# 递归
class Solution:
    def permute(self, nums):
        res = []
        self.recursion(nums, [], res)
        return res

    def recursion(self, nums, path, res):
        if len(nums) == len(path):
            res.append(path)
        for i in list(set(nums).difference(set(path))):
            self.recursion(nums, path + [i], res)

    # def recursion(self, nums, path, res):
    #     if not nums:
    #         res.append(path)
    #     for i in range(len(nums)):
    #         self.recursion(nums[:i] + nums[i + 1:], path + [nums[i]], res)

