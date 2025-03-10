from functools import cache
from typing import List


"""
题目：63. 不同路径 II

给定一个 m x n 的整数数组 grid。一个机器人初始位于 左上角（即 grid[0][0]）。机器人尝试移动到 右下角（即 grid[m - 1][n - 1]）。机器人每次只能向下或者向右移动一步。

网格中的障碍物和空位置分别用 1 和 0 来表示。机器人的移动路径中不能包含 任何 有障碍物的方格。

返回机器人能够到达右下角的不同路径数量。

测试用例保证答案小于等于 2 * 109。

"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache
        def dfs(x: int, y: int) -> int:
            if x < 0 or y < 0:
                return 0
            if obstacleGrid[x][y] == 1:
                return 0
            if x == 0 and y == 0:
                return 1
            return dfs(x - 1, y) + dfs(x, y - 1)

        return dfs(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)

    @staticmethod
    def uniquePathsWithObstacles_2(obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j]

        return dp[m][n]

    def uniquePathsWithObstacles_3(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        dp = [0] * (n+1)
        dp[1] = 1

        for row in obstacleGrid:
            for j,x in enumerate(row):
                if x == 0:
                    dp[j+1] += dp[j]
                else:
                    dp[j+1] = 0

        return dp[n]