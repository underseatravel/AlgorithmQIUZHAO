#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 21:57
# @Author  : weiyu
# @File    : 552_student_attendance_record2.py


class Solution:
    def checkRecord(self, n):
        if n == 1: return 3
        if n == 0: return 0
        mod = 10**9 + 7
        dp = [0 for _ in range(n + 1)]
        dp[0], dp[1], dp[2] = 1, 2, 4
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % mod
        res = dp[n]
        for i in range(1, n + 1):
            res += dp[i - 1] * dp[n - i] % mod
        res = res % mod
        return res
