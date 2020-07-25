#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 18:46
# @Author  : weiyu
# @File    : 347_top_k_frequent_element.py
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        res = []
        dict = {}
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        heap = [(-val, key) for key, val in dict.items()]
        heapq.heapify(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res