#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 23:55
# @Author  : weiyu
# @File    : 338_counting_bits.py



class Solution:
    def countBits(self, num):
        dp = [0 for _ in range(num + 1)]
        for i in range(1, num + 1):
            if i & 1 == 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i // 2]
        return dp



