#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 23:48
# @Author  : weiyu
# @File    : 874_walking_robot_simulation.py


class Solution:
    def robotSim(self, commands, obstacles):
        i = j = res = d = 0
        move = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        obstacles = set(map(tuple, obstacles))
        for command in commands:
            if command == -2: d = (d + 1) % 4
            elif command == -1: d = (d - 1) % 4
            else:
                x, y = move[d]
                while command and (i + x, j + y) not in obstacles:
                    i += x
                    j += y
                    command -= 1
            res = max(res, i ** 2 + j ** 2)
        return res