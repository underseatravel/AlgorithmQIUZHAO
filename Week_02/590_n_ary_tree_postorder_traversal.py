#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 0:36
# @Author  : weiyu
# @File    : 590_n_ary_tree_postorder_traversal.py

class Solution:
    def postorder(self, root):
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if root:
            for child in root.children:
                self.dfs(child, res)
            res.append(root.val)
