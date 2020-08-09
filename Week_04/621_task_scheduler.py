#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 0:13
# @Author  : weiyu
# @File    : 621_task_scheduler.py
import collections

# greedy
class Solution:
    def leastInterval(self, tasks, n):
        task_counts = list(collections.Counter(tasks).values())
        m = max(task_counts)
        mct = task_counts.count(m)
        return max(len(tasks), (m - 1) * (n + 1) + mct)
