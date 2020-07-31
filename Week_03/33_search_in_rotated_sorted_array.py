#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/31 1:37
# @Author  : weiyu
# @File    : 33_search_in_rotated_sorted_array.py


class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
