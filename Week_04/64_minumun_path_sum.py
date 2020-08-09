#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 18:06
# @Author  : weiyu
# @File    : 64_minumun_path_sum.py

# DP Time O(mn)  Space O(mn)
class Solution:
    def minPathSum(self, grid):
        dp = grid
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            dp[i][0] += dp[i - 1][0]
        for j in range(1, n):
            dp[0][j] += dp[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

# DP Time O(mn) Space O(n)
class Solution:
    def minPathSum(self, grid):
        dp = grid[0]
        m, n = len(grid), len(grid[0])
        for j in range(1, n):
            dp[j] += dp[j - 1]
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = grid[i][j] + min(dp[j], dp[j - 1])
        return dp[-1]