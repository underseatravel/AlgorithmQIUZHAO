#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 0:43
# @Author  : weiyu
# @File    : 589_n_ary_tree_preorder_traversal.py


class Solution:
    def preorder(self, root):
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if root:
            res.append(root.val)
            for child in root.children:
                self.dfs(child, res)
