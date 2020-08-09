#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 23:35
# @Author  : weiyu
# @File    : 221_maximal_square.py


class Solution:
    def maximalSquare(self, matrix):
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        maxside = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                maxside = max(maxside, dp[i][j])
        return maxside * maxside

