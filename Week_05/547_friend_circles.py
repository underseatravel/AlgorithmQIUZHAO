#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 21:45
# @Author  : weiyu
# @File    : 547_friend_circles.py

# DFS  time O(n^2)  Space O(n)
class Solution:
    def findCircleNum(self, M):
        if not M: return 0
        n = len(M)
        count = 0
        self.visited = set()
        for i in range(n):
            if i not in self.visited:
                self.visited.add(i)
                self.dfs(i, M)
                count += 1
        return count

    def dfs(self, node, M):
        for nei, adj in enumerate(M[node]):
            if adj and nei not in self.visited:
                self.visited.add(nei)
                self.dfs(nei, M)

# unionfind  time O(n^3)  Space O(n)
class Solution:
    def findCircleNum(self, M):
        if not M: return 0
        n = len(M)
        p = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    self.union(p, i, j)
        return len(set(self.parent(p, i) for i in range(n)))

    def union(self, p, i, j):
        p1 = self.parent(p, i)
        p2 = self.parent(p, j)
        p[p2] = p1

    def parent(self, p, i):
        root = p[i]
        while p[root] != root:
            root = p[root]
        return root
