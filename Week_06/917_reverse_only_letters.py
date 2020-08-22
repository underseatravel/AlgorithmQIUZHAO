#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 22:32
# @Author  : weiyu
# @File    : 917_reverse_only_letters.py

# 双指针
class Solution:
    def reverseOnlyLetters(self, S):
        S = list(S)
        i, j = 0, len(S) - 1
        while i < j:
            while i < j and not S[i].isalpha(): i += 1
            while i < j and not S[j].isalpha(): j -= 1
            S[i], S[j] = S[j], S[i]
            i += 1
            j -= 1
        return "".join(S)