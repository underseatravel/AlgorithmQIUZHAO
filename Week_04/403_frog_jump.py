#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 19:25
# @Author  : weiyu
# @File    : 403_frog_jump.py

# DP Time O(n^2)  Space O(n^2) -> hashmap最大可能到n^2
class Solution:
    def canCross(self, stones):
        d = dict((x, set()) for x in stones)
        if stones[1] != 1: return False

        d[1].add(1)
        for x in stones[:-1]:
            for j in d[x]:
                for k in range(j - 1, j + 2):
                    if k > 0 and x + k in d:
                        d[x + k].add(k)
        return d[stones[-1]] != set()
