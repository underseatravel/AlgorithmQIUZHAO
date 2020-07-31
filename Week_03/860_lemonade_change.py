#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 20:53
# @Author  : weiyu
# @File    : 860_lemonade_change.py


class Solution:
    def lemonadeChange(self, bills):
        five = ten = 0
        for i in bills:
            if i == 5: five += 1
            elif i == 10: five -= 1; ten += 1
            elif i == 20:
                if ten:
                    ten -= 1; five -= 1
                else:
                    five -= 3
            if five < 0:
                return False
        return True