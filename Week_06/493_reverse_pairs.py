#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 0:36
# @Author  : weiyu
# @File    : 493_reverse_pairs.py


class Solution:
    def reversePairs(self, nums):
        if not nums: return 0
        self.cnt = 0
        left, right = 0, len(nums) - 1
        self.mergesort(nums, left, right)
        return self.cnt

    def mergesort(self, nums, left, right):
        if right <= left: return
        mid = (left + right) // 2
        self.mergesort(nums, left, mid)
        self.mergesort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        tmp = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if nums[i] > 2 * nums[j]:
                self.cnt += mid - i + 1
                j += 1
            else:
                i += 1
        # i = left
        # j = mid + 1
        # while i <= mid and j <= right:
        #     if nums[i] <= nums[j]:
        #         tmp.append(nums[i])
        #         i += 1
        #     else:
        #         tmp.append(nums[j])
        #         j += 1
        # while i <= mid:
        #     tmp.append(nums[i])
        #     i += 1
        # while j <= right:
        #     tmp.append(nums[j])
        #     j += 1
        # nums[left: right + 1] = tmp
        nums[left:right + 1] = sorted(nums[left: right + 1])