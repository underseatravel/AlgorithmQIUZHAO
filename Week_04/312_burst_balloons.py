#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 23:53
# @Author  : weiyu
# @File    : 312_burst_balloons.py


class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[j] * nums[k])
        return dp[0][-1]