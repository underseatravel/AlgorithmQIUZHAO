#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 20:46
# @Author  : weiyu
# @File    : 56_merge_intervals.py


class Solution:
    def mergeIntervals(self, intervals):
        intervals.sort(key = lambda x:x[0])
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res