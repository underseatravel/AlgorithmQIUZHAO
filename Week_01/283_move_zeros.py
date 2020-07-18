#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 11:22
# @Author  : weiyu
# @File    : 283_move_zeros.py

class Solution:
    def moveZeros(self, nums):
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1


t = Solution()

nums = [0, 1, 0, 3, 12]
t.moveZeros(nums)
print(nums)

nums = [0, 1, 3, 0, 9, 0, 0]
t.moveZeros(nums)
print(nums)
