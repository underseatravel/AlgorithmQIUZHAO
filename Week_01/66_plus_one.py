#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 19:32
# @Author  : weiyu
# @File    : 66_plus_one.py


# int str转化法
class Solution:
    def plusOne(self, digits):
        num = int("".join([str(c) for c in digits]))
        num += 1
        return [int(c) for c in str(num)]


# 倒序遍历
class Solution:
    def plusOne(self, digits):
        for i in range(1, len(digits) + 1):
            if digits[-i] != 9:
                digits[-i] += 1
                return digits
            digits[-i] = 0
        digits.insert(0, 1)
        return digits