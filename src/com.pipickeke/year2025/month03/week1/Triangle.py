from functools import cache
from typing import List

"""
题目：120. 三角形最小路径和

给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。



"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        @cache
        def dfs(x: int, y: int) -> int:
            if x == n - 1:
                return triangle[x][y]

            return triangle[x][y] + min(
                dfs(x + 1, y), dfs(x + 1, y + 1)
            )

        return dfs(0, 0)

    def minimumTotal_2(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * (i + 1) for i in range(n)]
        dp[-1] = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j, x in enumerate(triangle[i]):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + x

        return dp[0][0]
