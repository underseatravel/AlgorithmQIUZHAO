#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 22:16
# @Author  : weiyu
# @File    : 122_best_time_to_buy_and_sell_stock2.py

# greedy
class Solution:
    def maxProfit(self, prices):
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res

class Solution:
    def maxProfit(self, prices):
        return sum(b - a for a, b in zip(prices[:-1], prices[1:]) if b > a)