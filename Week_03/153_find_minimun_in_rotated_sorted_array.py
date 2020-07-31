#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/31 2:50
# @Author  : weiyu
# @File    : 153_find_minimun_in_rotated_sorted_array.py


class Solution:
    def findMin(self, nums):
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid
        return nums[i]