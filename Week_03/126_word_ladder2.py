#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 1:23
# @Author  : weiyu
# @File    : 126_word_ladder2.py
import collections

# BFS
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                    return res
                else:
                    for i in range(len(w)):
                        for c in "abcdefghijklmnopqrstuvwxyz":
                            new = w[:i] + c + w[i + 1:]
                            if new in wordList:
                                newlayer[new] += [j + [new] for j in layer[w]]
            wordList -= set(newlayer.keys())
            layer = newlayer
        return res