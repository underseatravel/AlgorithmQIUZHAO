#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 10:34
# @Author  : weiyu
# @File    : 541_reverse_string2.py


class Solution:
    def reverseStr(self, s, k):
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i + k] = reversed(s[i:i + k])
        return "".join(s)


class Solution:
    def reverseStr(self, s, k):
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i + k] = reversed(s[i:i + k])
        return "".join(s)