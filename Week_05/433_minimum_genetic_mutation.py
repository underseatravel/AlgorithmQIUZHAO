#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 21:15
# @Author  : weiyu
# @File    : 433_minimum_genetic_mutation.py
import collections

class Solution:
    def minMutation(self, start, end, bank):
        bank = set(bank)
        if end not in bank: return -1
        queue = collections.deque([(start, 0)])
        while queue:
            node, step = queue.popleft()
            if node == end:
                return step
            for i in range(len(node)):
                for j in "ACGT":
                    new = node[:i] + j + node[i + 1:]
                    if new in bank:
                        queue.append((new, step + 1))
                        bank.remove(new)
        return -1