#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 1:29
# @Author  : weiyu
# @File    : 45_jump_game.py


# 从前往后 贪心
class Solution:
    def jump(self, nums):
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
