#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 23:09
# @Author  : weiyu
# @File    : 76_minimum_window_substring.py
import collections

# 滑窗思想
class Solution:
    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]