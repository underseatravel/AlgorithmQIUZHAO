#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 0:23
# @Author  : weiyu
# @File    : 55_jump_game2.py

# 从前往后
class Solution:
    def canJump(self, nums):
        max_len = 0
        for i, n in enumerate(nums):
            if max_len < i:
                return False
            max_len = max(max_len, i + n)
        return True


# 从后往前
class Solution:
    def canJump(self, nums):
        can_reach = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= can_reach:
                can_reach = i
        return can_reach == 0