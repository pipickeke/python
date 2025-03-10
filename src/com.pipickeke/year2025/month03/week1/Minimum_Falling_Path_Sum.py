from cmath import inf
from functools import cache
from typing import List

"""
题目：931. 下降路径最小和

给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。

下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多
相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。具体来说，位置 (row, col) 的下一个元素
应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。

"""

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        @cache
        def dfs(x: int, y: int):
            if y < 0 or y >= n:
                return inf
            if x == n - 1:
                return matrix[x][y]

            return matrix[x][y] + min(dfs(x + 1, y - 1), dfs(x + 1, y), dfs(x + 1, y + 1))

        return min(dfs(0, i) for i in range(n))

    def minFallingPathSum_2(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(n):
                if i == n - 1:
                    dp[i][j] = matrix[i][j]
                else:
                    left = dp[i + 1][j - 1] if j-1 >= 0 else float('inf')
                    right =dp[i + 1][j + 1] if j+1 < n else float('inf')
                    dp[i][j] = matrix[i][j] + min(dp[i + 1][j], min(left, right))

        return min(dp[0])
