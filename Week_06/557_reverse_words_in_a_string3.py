#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 10:54
# @Author  : weiyu
# @File    : 557_reverse_words_in_a_string3.py


class Solution:
    def reverseWords(self, s):
        return " ".join(c[::-1] for c in s.split())
