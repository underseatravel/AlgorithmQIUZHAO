#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 16:13
# @Author  : weiyu
# @File    : 32_longest_valid_parentheses.py


class Solution:
    def longestValidParentheses(self, s):
        if not s: return 0
        n = len(s)
        dp = [0 for _ in range(n)]
        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
        return max(dp)