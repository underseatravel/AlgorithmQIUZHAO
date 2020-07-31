#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/31 2:20
# @Author  : weiyu
# @File    : 74_search_a_2D_matrix.py

# 转化为一维
class Solution:
    def searchMatrix(self, matrix, target):
        nums = []
        for k in matrix:
            nums.extend(k)
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

# 二维二分查找
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix: return False
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid // cols][mid % cols]
            if num == target:
                return True
            elif num > target:
                high = mid - 1
            else:
                low = mid + 1
        return False