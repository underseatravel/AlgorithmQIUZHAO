#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 18:23
# @Author  : weiyu
# @File    : 363_max_sum_of_rectangle_no_larger_than_k.py
import bisect


# 固定左右边界 + 最大子序和（一维数组存每行的和）   的思想
class Solution:
    def maxSumSubmatrix(self, matrix, k):
        if not matrix: return 0
        row, col = len(matrix), len(matrix[0])
        res = float("-inf")
        for left in range(col):
            _sum = [0] * row
            for right in range(left, col):
                for i in range(row):
                    _sum[i] += matrix[i][right]

                arr = [0]
                cur = 0
                for num in _sum:
                    cur += num
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr):
                        res = max(res, cur - arr[loc])
                    bisect.insort(arr, cur)
        return res
