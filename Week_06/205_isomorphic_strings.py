#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 13:48
# @Author  : weiyu
# @File    : 205_isomorphic_strings.py


class Solution:
    def isIsomorphic(self, s, t):
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())