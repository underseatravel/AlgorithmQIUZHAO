#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 22:44
# @Author  : weiyu
# @File    : 455_assign_cookies.py


class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i