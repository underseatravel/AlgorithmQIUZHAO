#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 10:41
# @Author  : weiyu
# @File    : 5_longest_palindromic_substring.py

# 中心扩散法。时间O(n)
class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            odd_str = self.palindrome(s, i, i)
            even_str = self.palindrome(s, i, i + 1)
            if len(odd_str) > len(res):
                res = odd_str
            if len (even_str) > len(res):
                res = even_str
        return res


    def palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]
