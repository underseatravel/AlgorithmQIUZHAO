#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 1:05
# @Author  : weiyu
# @File    : 647_palindromic_substrings.py

# Dp Time O(n^2)  Space O(n^2)
class Solution:
    def countSubstrings(self, s):
        n = len(s)
        res = 0
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    dp[i][j] = j - i < 2 or dp[i + 1][j - 1]
                    res += dp[i][j]
        return res


# 中心扩散法  Time O(n^2)
class Solution:
    def countSubstrings(self, s):
        self.res = 0
        for i in range(len(s)):
            self.palindrome(s, i, i)
            self.palindrome(s, i, i + 1)
        return self.res

    def palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            self.res += 1
