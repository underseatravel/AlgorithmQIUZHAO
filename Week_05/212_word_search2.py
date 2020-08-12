#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 18:08
# @Author  : weiyu
# @File    : 212_word_search2.py


class Solution:
    def findWords(self, board, words):
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node["#"] = True

        self.res, self.m, self.n = set(), len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in trie:
                    self.dfs(i, j, trie[board[i][j]], board[i][j], {(i, j)}, board)
        return list(self.res)

    def dfs(self, i, j, node, pre, visited, board):
        if "#" in node:
            self.res.add(pre)
        for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            x, y = i + d[0], j + d[1]
            if 0 <= x < self.m and 0 <= y < self.n and board[x][y] in node and (x, y) not in visited:
                self.dfs(x, y, node[board[x][y]], pre + board[x][y], visited | {(x, y)}, board)
