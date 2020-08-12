#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 22:50
# @Author  : weiyu
# @File    : 130_surrounded_regions.py

# DPS Time O(n^2) Space O(1)
class Solution:
    def solve(self, board):
        if not board: return []
        m, n = len(board), len(board[0])
        for i in range(m):
            if board[i][0] == "O": self.dfs(i, 0, board)
            if board[i][n - 1] == "O": self.dfs(i, n - 1, board)
        for j in range(n):
            if board[0][j] == "O": self.dfs(0, j, board)
            if board[m - 1][j] == "O": self.dfs(m - 1, j, board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O": board[i][j] = "X"
                if board[i][j] == "B": board[i][j] = "O"

    def dfs(self, i, j, board):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != "O":
            return
        board[i][j] = "B"
        for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            x, y = i + d[0], j + d[1]
            self.dfs(x, y, board)

