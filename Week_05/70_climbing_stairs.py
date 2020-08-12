#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 15:53
# @Author  : weiyu
# @File    : 70_climbing_stairs.py

class Solution:
    def climbStairs(self, n):
        if n == 1 or n ==2:
            return n
        a, b, temp = 1, 2, 0
        for i in range(3, n + 1):
            temp = a + b
            a = b
            b = temp
        return temp

t = Solution()
print(t.climbStairs(2))
print(t.climbStairs(3))