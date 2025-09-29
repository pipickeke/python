"""


"""
from functools import cache
from math import inf
from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @cache
        def dfs(i,j):
            if j > i:
                return 0
            if i < 0:
                return inf

            return min(dfs(i-1, j-1),
                       dfs(i-1, j+time[i])+cost[i])

        return dfs(len(cost)-1, 0)


