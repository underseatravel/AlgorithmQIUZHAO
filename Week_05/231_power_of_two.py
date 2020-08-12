#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 23:16
# @Author  : weiyu
# @File    : 231_power_of_two.py


class Solution:
    def isPowerOfTwo(self, n):
        return n > 0 and n & (n - 1) == 0
