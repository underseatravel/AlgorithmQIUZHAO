#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 16:32
# @Author  : weiyu
# @File    : 1_two_sum.py

# 暴力法
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# 哈希表
# class Solution:
#     def twoSum(self, nums, target):
#         if len(nums) <= 1:
#             return False
#         buff_dict = {}
#         for i in range(len(nums)):
#             if nums[i] in buff_dict:
#                 return [buff_dict[nums[i]], i]
#             else:
#                 buff_dict[target - nums[i]] = i



t = Solution()
print(t.twoSum([2, 7, 11, 15], 9))
