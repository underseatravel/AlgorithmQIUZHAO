#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 20:50
# @Author  : weiyu
# @File    : 105_construst_binary_tree_from_preorder_and_inorder_traversal.py

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left, self.right = None, None


class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[idx])
            root.left = self.buildTree(preorder, inorder[:idx])
            root.right = self.buildTree(preorder, inorder[idx + 1:])
            return root