#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 0:55
# @Author  : weiyu
# @File    : 51_n_queens.py

# 递归
# class Solution:
#     def solveNQueens(self, n):
#         self.res = []
#         self.cols = set(); self.pie = set(); self.na = set()
#         self.dfs(n, 0, [])
#         return self._generate_result(n)
#
#     def dfs(self, n, row, status):
#         if row == n:
#             self.res.append(status)
#             return
#
#         for col in range(n):
#             if col in self.cols or row + col in self.pie or row - col in self.na:
#                 continue
#             self.cols.add(col)
#             self.pie.add(row + col)
#             self.na.add(row - col)
#             self.dfs(n, row + 1, status + [col])
#
#             self.cols.remove(col)
#             self.pie.remove(row + col)
#             self.na.remove(row - col)
#
#     def _generate_result(self, n):
#         block = []
#         for ch in self.res:
#             for i in ch:
#                 block.append("."*i + "Q" + "."*(n - i -1))
#         return [block[i:i+n] for i in range(0, len(block), n)]


# 递归精简
class Solution:
    def solveNQueens(self, n):
        self.res = []
        self.dfs([],[],[], n)
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in self.res]

    def dfs(self, cols, pie, na, n):
        row = len(cols)
        if row == n:
            self.res.append(cols)

        for col in range(n):
            if col not in cols and row + col not in pie and row - col not in na:
                self.dfs(cols + [col], pie + [row + col], na + [row - col], n)


