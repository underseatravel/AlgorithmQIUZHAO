#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 16:26
# @Author  : weiyu
# @File    : 50_powx_n.py

# 分治
class Solution:
    def myPow(self, x, n):
        if n < 0:
            return 1 / self.recursion(x, -n)
        else:
            return self.recursion(x, n)

    def recursion(self, x, n):
        if n == 0: return 1
        half = self.recursion(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

# 暴力
class Solution:
    def myPow(self, x, n):
        if n < 0:
            n = -n
            x = 1 / x
        res = 1
        for i in range(n):
            res *= x
        return res