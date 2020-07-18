#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 21:31
# @Author  : weiyu
# @File    : 641_design_circular_deque.py


class MyCircularDeque:
    def __init__(self, k):
        self.max_size = k
        self.queue = []

    def insertFront(self, value):
        if len(self.queue) < self.max_size:
            self.queue.insert(0, value)
            return True
        return False


    def insertLast(self, value):
        if len (self.queue) < self.max_size:
            self.queue.append(value)
            return True
        return False


    def deleteFront(self):
        if self.queue:
            del self.queue[0]
            return True
        return False

    def deleteLast(self):
        if self.queue:
            del self.queue[-1]
            return True
        return False


    def getFront(self):
        if self.queue:
            return self.queue[0]
        return -1


    def getRear(self):
        if self.queue:
            return  self.queue[-1]
        return -1


    def isEmpty(self):
        return not self.queue


    def isFull(self):
        return len(self.queue) == self.max_size

