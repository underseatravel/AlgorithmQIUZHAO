#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/20 0:01
# @Author  : weiyu
# @File    : 300_longest_increasing_subsequence.py

class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
