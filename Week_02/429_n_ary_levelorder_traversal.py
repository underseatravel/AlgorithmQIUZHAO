#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 1:26
# @Author  : weiyu
# @File    : 429_n_ary_levelorder_traversal.py


class Solution:
    def levelOrder(self, root):
        if not root: return []
        queue = [root]
        res = []
        while queue:
            res.append([node.val for node in queue])
            queue = [child for node in queue for child in node.children if child]
        return res