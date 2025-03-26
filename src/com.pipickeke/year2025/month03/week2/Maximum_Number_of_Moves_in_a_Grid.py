from functools import cache
from typing import List

"""
题目：2684. 矩阵中移动的最大次数

给你一个下标从 0 开始、大小为 m x n 的矩阵 grid ，矩阵由若干 正 整数组成。

你可以从矩阵第一列中的 任一 单元格出发，按以下方式遍历 grid ：

从单元格 (row, col) 可以移动到 (row - 1, col + 1)、(row, col + 1) 和 (row + 1, col + 1) 三个单元格中任一满足值 严格 大于当前单元格的单元格。
返回你在矩阵中能够 移动 的 最大 次数。

"""

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        ans = 0
        @cache
        def dfs(x: int, y: int) -> None:
            nonlocal ans
            ans = max(ans, y)

            if ans == n-1:
                return

            for k in x-1,x,x+1:
                if 0<=k<m and grid[k][y+1] > grid[x][y]:
                    dfs(k, y+1)

        for i in range(m):
            dfs(i, 0)

        return ans


    def maxMoves_2(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        q1 = set(range(m))
        for j in range(1,n):
            q2 = set()
            for i in q1:
                for k in i-1,i,i+1:
                    if 0<=k<m and grid[i][j-1] < grid[k][j]:
                        q2.add(k)
            q1 = q2
            if not q1:
                return j-1
        return n-1




