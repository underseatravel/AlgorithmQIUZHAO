#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 19:29
# @Author  : weiyu
# @File    : 17_letter_combination_of_a_phone_number.py

# 递归
class Solution:
    def letterCombinations(self, digits):
        self.dict = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9": "wxyz"}
        self.res = []
        if digits == "": return []
        self.recursion(digits, "")
        return self.res

    def recursion(self, digits, path):
        if digits == "":
            self.res.append(path)
            return
        for i in self.dict[digits[0]]:
            self.recursion(digits[1:], path + i)
