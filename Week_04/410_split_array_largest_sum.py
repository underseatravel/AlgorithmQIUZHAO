#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 21:02
# @Author  : weiyu
# @File    : 410_split_array_largest_sum.py


class Solution:
    def splitArray(self, nums, m):
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if self.check(mid, nums, m):
                right = mid
            else:
                left = mid + 1
        return left

    def check(self, x, nums, m):
        total, cnt = 0, 1
        for num in nums:
            if total + num > x:
                cnt += 1
                total = num
            else:
                total += num
        return cnt <= m
