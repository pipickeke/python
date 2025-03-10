from functools import cache

"""
题目：62. 不同路径

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(x: int, y: int) -> int:
            if x < 0 or y < 0:
                return 0
            if x == 0 and y == 0:
                return 1
            return dfs(x - 1, y) + dfs(x, y - 1)

        return dfs(m - 1, n - 1)

    def uniquePaths_2(self,m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[0][1] = 1
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1]
        return dp[m][n]








