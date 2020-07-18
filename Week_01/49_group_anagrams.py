#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 0:33
# @Author  : weiyu
# @File    : 49_group_anagrams.py

class Solution:
    def groupAnagrams(self, strs):
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            dict[key] = dict.get(key, []) + [item]
        return list(dict.values())


t = Solution()
print(t.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))