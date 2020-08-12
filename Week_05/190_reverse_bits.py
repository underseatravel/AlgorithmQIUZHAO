#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 23:34
# @Author  : weiyu
# @File    : 190_reverse_bits.py


class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
        return res