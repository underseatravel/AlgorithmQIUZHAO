#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 15:29
# @Author  : weiyu
# @File    : 26_remove_duplicates_in_sorted_array.py


class Solution:
    def removeDuplicates(self, nums):
        if not nums: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1

t = Solution()
print(t.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))