#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 20:17
# @Author  : weiyu
# @File    : lowest_common_ancestor_of_a_binary_tree.py


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root: return None
        if p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root
        if not left: return right
        if not right: return left