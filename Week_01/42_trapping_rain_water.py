#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 23:04
# @Author  : weiyu
# @File    : 42_trapping_rain_water.py


class Solution:
    def trap(self, height):
        stack = []
        res, idx = 0, 0
        length = len(height)
        if length < 3: return 0
        while idx < length:
            while stack and height[idx] > height[stack[-1]]:
                top = stack.pop()
                if stack == []:
                    break
                h = min(height[idx], height[stack[-1]]) - height[top]
                w = idx - stack[-1] - 1
                res += h * w
            stack.append(idx)
            idx += 1
        return res


t = Solution()
print(t.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

