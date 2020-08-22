#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 19:58
# @Author  : weiyu
# @File    : 1122_relative_sort_array.py

# 计数排序
class Solution:
    def relativeSortArray(self, arr1, arr2):
        arr = [0 for _ in range(1001)]
        res = []
        for i in range(len(arr1)):
            arr[arr1[i]] += 1
        for i in range(len(arr2)):
            while arr[arr2[i]] > 0:
                res.append(arr2[i])
                arr[arr2[i]] -= 1
        for i in range(len(arr)):
            while arr[i] > 0:
                res.append(i)
                arr[i] -= 1
        return res