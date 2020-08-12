#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 23:36
# @Author  : weiyu
# @File    : 127_word_ladder.py
import collections

# BFS
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        bank = set(wordList)
        queue = collections.deque([(beginWord, 1)])
        if endWord not in wordList: return 0
        while queue:
            node, step = queue.popleft()
            if node == endWord:
                return step
            for i in range(len(node)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new = node[:i] + c + node[i + 1:]
                    if new in bank:
                        queue.append((new, step + 1))
                        bank.remove(new)
        return 0

