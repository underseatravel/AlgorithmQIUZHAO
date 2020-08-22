#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 2:15
# @Author  : weiyu
# @File    : 151_reverse_words_in_a_string.py

class Solution:
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])
