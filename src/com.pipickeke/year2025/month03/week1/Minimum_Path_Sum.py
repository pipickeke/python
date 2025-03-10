from functools import cache
from math import inf
from typing import List

"""
64. 最小路径和

给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dfs(x: int, y: int) -> int:
            if x < 0 or y < 0:
                return inf
            if x == 0 and y == 0:
                return grid[x][y]
            return min(dfs(x - 1, y), dfs(x, y - 1)) + grid[x][y]

        return dfs(len(grid) - 1, len(grid[0]) - 1)


    def minPathSum_2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[inf] * (n+1) for _ in range(m+1)]
        f[0][1] = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                f[i+1][j+1] = min(f[i+1][j], f[i][j+1]) + x

        return f[m][n]





