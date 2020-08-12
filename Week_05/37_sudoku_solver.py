#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 19:12
# @Author  : weiyu
# @File    : 37_sudoku_solver.py


class Solution:
    def solveSudoku(self, board):
        self.row = [set(range(1, 10)) for _ in range(9)]
        self.col = [set(range(1, 10)) for _ in range(9)]
        self.block = [set(range(1, 10)) for _ in range(9)]
        self.empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    val = int(board[i][j])
                    self.row[i].remove(val)
                    self.col[j].remove(val)
                    self.block[(i//3)*3 + j//3].remove(val)
                else:
                    self.empty.append((i, j))
        self.dfs(board)

    def dfs(self, board, iter = 0):
        if iter == len(self.empty):
            return True
        i, j = self.empty[iter]
        b = (i//3)*3 + j//3
        for val in self.row[i] & self.col[j] & self.block[b]:
            self.row[i].remove(val)
            self.col[j].remove(val)
            self.block[b].remove(val)
            board[i][j] = str(val)
            if self.dfs(board, iter + 1):
                return True
            self.row[i].add(val)
            self.col[j].add(val)
            self.block[b].add(val)
        return False