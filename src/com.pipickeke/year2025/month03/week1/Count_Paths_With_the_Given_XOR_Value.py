from functools import cache
from typing import List

"""
题目：3393. 统计异或值为给定值的路径数目

给你一个大小为 m x n 的二维整数数组 grid 和一个整数 k 。

你的任务是统计满足以下 条件 且从左上格子 (0, 0) 出发到达右下格子 (m - 1, n - 1) 的路径数目：

每一步你可以向右或者向下走，也就是如果格子存在的话，可以从格子 (i, j) 走到格子 (i, j + 1) 或者格子 (i + 1, j) 。
路径上经过的所有数字 XOR 异或值必须 等于 k 。
请你返回满足上述条件的路径总数。

由于答案可能很大，请你将答案对 109 + 7 取余 后返回。

"""

class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        MOD = 1_000_000_007
        @cache
        def dfs(x, y, k):
            if x < 0 or y < 0:
                return 0
            if x == 0 and y == 0:
                return 1 if grid[0][0] == k else 0
            return (dfs(x - 1, y, k ^ grid[x][y]) + dfs(x, y - 1, k ^ grid[x][y])) %MOD

        return dfs(m - 1, n - 1, k)

    def countPathsWithXorValue_2(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 1_000_000_007

        u = 1 << max(map(max, grid)).bit_length()
        if k >= u:
            return 0

        dp = [[[0] * u for _ in range(n+1)] for _ in range(m+1)]
        dp[0][1][0] = 1
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                for x in range(u):
                    dp[i+1][j+1][x] = (dp[i+1][j][x ^ val] + dp[i][j+1][x ^ val]) %MOD

        return dp[m][n][k]













