#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 0:06
# @Author  : weiyu
# @File    : 94_binary_tree_inorder_traversal.py

# recursion
class Solution:
    def inorderTraversal(self, root):
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if root:
            self.dfs(root.left, res)
            res.append(root.val)
            self.dfs(root.right, res)