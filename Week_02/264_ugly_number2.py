#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 17:35
# @Author  : weiyu
# @File    : 264_ugly_number2.py
import heapq

class Solution:
    def nthUglyNumber(self, n):
        heap = [1]
        visited = set([1])
        for i in range(n):
            val = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                next_val = factor * val
                if next_val not in visited:
                    heapq.heappush(heap, next_val)
                    visited.add(next_val)
        return val

