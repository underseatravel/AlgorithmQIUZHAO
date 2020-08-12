#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 23:59
# @Author  : weiyu
# @File    : 52_n_queens2.py



class Solution:
    def totalNQueens(self, n):
        self.res = []
        self.dfs([], [], [], n)
        return len(self.res)

    def dfs(self, cols, pie, na, n):
        row = len(cols)
        if row == n:
            self.res.append(cols)
        for col in range(n):
            if col not in cols and row + col not in pie and row - col not in na:
                self.dfs(cols + [col], pie + [row + col], na + [row - col], n)
