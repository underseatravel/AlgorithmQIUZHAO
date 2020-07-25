#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 0:22
# @Author  : weiyu
# @File    : 144_binary_tree_preorder_traversal.py


class Solution:
    def preorderTraversal(self, root):
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if root:
            res.append(root.val)
            self.dfs(root.left, res)
            self.dfs(root.right, res)
