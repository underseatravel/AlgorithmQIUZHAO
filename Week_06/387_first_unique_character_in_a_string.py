#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 0:16
# @Author  : weiyu
# @File    : 387_first_unique_character_in_a_string.py


class Solution:
    def firstUniqChar(self, s):
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        for i, c in enumerate(s):
            if dic[c] == 1:
                return i
        return -1