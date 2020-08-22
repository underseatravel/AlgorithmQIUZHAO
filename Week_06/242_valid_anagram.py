#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 23:58
# @Author  : weiyu
# @File    : 242_valid_anagram.py


# 字典
class Solution:
    def isAnagram(self, s, t):
        dict1, dict2 = {}, {}
        for item in s:
            dict1[item] = dict1.get(item, 0) + 1
        for item in t:
            dict2[item] = dict2.get(item, 0) + 1
        return dict1 == dict2

# # 暴力sort
# class Solution:
#     def isAnagram(self, s, t):
#         return sorted(s) == sorted(t)

t = Solution()
print(t.isAnagram(s = "anagram", t = "nagaram"))
print(t.isAnagram(s = "anagram", t = "nasaram"))

