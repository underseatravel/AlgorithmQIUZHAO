#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 12:07
# @Author  : weiyu
# @File    : 36_valid_suduku.py


class Solution:
    def isValidSudoku(self, board):
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        blocks = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    num = int(num)
                    block_idx = (i // 3) * 3 + j // 3

                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    blocks[block_idx][num] = blocks[block_idx].get(num, 0) + 1

                    if rows[i][num] > 1 or cols[j][num] > 1 or blocks[block_idx][num] > 1:
                        return False
        return True