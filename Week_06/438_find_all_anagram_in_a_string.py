#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 12:12
# @Author  : weiyu
# @File    : 438_find_all_anagram_in_a_string.py
import collections

class Solution:
    def findAnagrams(self, s, p):
        res = []
        pdic = collections.Counter(p)
        sdic = collections.Counter(s[:len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            sdic[s[i]] += 1
            if sdic == pdic:
                res.append(i - len(p) + 1)
            sdic[s[i - len(p) + 1]] -= 1
            if sdic[s[i - len(p) + 1]] == 0:
                del sdic[s[i - len(p) + 1]]
        return res
