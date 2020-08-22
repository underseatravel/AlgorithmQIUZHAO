#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/20 1:39
# @Author  : weiyu
# @File    : 115_distinct_subsequences.py


class Solution:
    def numDistinct(self, s, t):
        m, n = len(t), len(s)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for j in range(n + 1):
            dp[0][j] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]