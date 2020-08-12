#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 1:09
# @Author  : weiyu
# @File    : 22_generate_parentheses.py

# DFS 递归
class Solution:
    def generateParenthesis(self, n):
        res = []
        self.recursion(n, n, "", res)
        return res

    def recursion(self, left, right, s, res):
        if left == 0 and right == 0:
            res.append(s)
            return
        if left > 0:
            self.recursion(left - 1, right, s + "(", res)
        if right > left:
            self.recursion(left, right - 1, s + ")", res)