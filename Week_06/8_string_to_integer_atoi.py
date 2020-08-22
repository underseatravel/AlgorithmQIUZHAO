#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 0:40
# @Author  : weiyu
# @File    : 8_string_to_integer_atoi.py



class Solution:
    def myAtoi(self, str):
        s = list(str.strip())
        if len(s) == 0: return 0
        sign = -1 if s[0] == "-" else 1
        if s[0] in ["+", "-"]:
            del s[0]
        res, i = 0, 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        return max(-2 ** 31, min(res * sign, 2 ** 31 - 1))