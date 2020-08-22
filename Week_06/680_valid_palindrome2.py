#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 13:30
# @Author  : weiyu
# @File    : 680_valid_palindrome2.py


class Solution:
    def validPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                one, two = s[l:r], s[l + 1:r + 1]
                return one == one[::-1] or two == two[::-1]
            l += 1
            r -= 1
        return True