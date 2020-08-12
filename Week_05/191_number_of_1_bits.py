#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 23:02
# @Author  : weiyu
# @File    : 191_number_of_1_bits.py

class Solution:
    def hammingWeight(self, n):
        sum = 0
        while n != 0:
            sum += 1
            n = n & (n - 1)
        return sum



