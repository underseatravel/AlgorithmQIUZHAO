#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 17:50
# @Author  : weiyu
# @File    : 169_majority_element.py

# sort法
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

# 哈希
class Solution:
    def majorityElement(self, nums):
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        for key in dict.keys():
            if dict[key] > len(nums)//2:
                return key



# 分治
class Solution:
    def majorityElement(self, nums):
        if len(nums) == 1: return nums[0]
        a = self.majorityElement(nums[:len(nums)//2])
        b = self.majorityElement(nums[len(nums)//2:])
        if a == b:
            return a
        return a if nums.count(a) > len(nums)//2 else b