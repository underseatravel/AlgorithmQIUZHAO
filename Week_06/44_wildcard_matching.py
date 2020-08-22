#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 17:41
# @Author  : weiyu
# @File    : 44_wildcard_matching.py


class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = True
            else:
                break
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] | dp[i][j - 1]
                elif p[j - 1] in [s[i - 1], "?"]:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]