"""

2742. 给墙壁刷油漆

给你两个长度为 n 下标从 0 开始的整数数组 cost 和 time ，
分别表示给 n 堵不同的墙刷油漆需要的开销和时间。你有两名油漆匠：

一位需要 付费 的油漆匠，刷第 i 堵墙需要花费 time[i] 单位的时间，
开销为 cost[i] 单位的钱。
一位 免费 的油漆匠，刷 任意 一堵墙的时间为 1 单位，开销为 0 。
但是必须在付费油漆匠 工作 时，免费油漆匠才会工作。
请你返回刷完 n 堵墙最少开销为多少。

"""
from cmath import inf
from functools import cache
from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @cache
        def dfs(i, j):
            if j > i:
                return 0

            if i < 0:
                return inf

            return min(dfs(i-1, j-1),
                       dfs(i-1,j+time[i])+cost[i])

        return dfs(len(cost)-1,0)



    def paintWalls_2(self, cost: List[int], time: List[int]) -> int:
        @cache
        def dfs(i,j):
            if j > i:
                return 0

            if i < 0:
                return inf

            return min(dfs(i-1,j-1),
                       dfs(i-1,j+time[i])+cost[i])
        return dfs(len(cost)-1,0)









