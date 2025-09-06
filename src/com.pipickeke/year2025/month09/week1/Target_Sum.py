"""
494. 目标和

给你一个非负整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。


"""
from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums:List[int], target: int) -> int:
        if sum(nums) < abs(target):
            return 0

        @cache
        def dfs(i, j):
            if i < 0:
                return 1 if j == 0 else 0

            return dfs(i-1, j-nums[i]) + dfs(i-1, j+nums[i])

        return dfs(len(nums)-1, target)


    def findTargetSumWays_2(self, nums:List[int], target: int) -> int:
        s = sum(nums) - abs(target)
        if s < 0 or s % 2:
            return 0

        @cache
        def dfs(i, j):
            if i < 0:
                return 1 if j == 0 else 0

            if j < nums[i]:
                return dfs(i-1, j)

            return dfs(i-1, j-nums[i]) + dfs(i-1, j)

        m = (sum(nums) - abs(target)) // 2
        return dfs(len(nums)-1, m)


    def findTargetSumWays_3(self, nums: List[int], target: int) -> int:
        s = sum(nums) - abs(target)
        if s < 0 or s % 2:
            return 0

        m = s // 2
        n = len(nums)

        f = [[0] * (m+1) for _ in range(n+1)]
        f[0][0] = 1

        for i, x in enumerate(nums):
            for c in range(m+1):
                if c < nums[i]:
                    f[i+1][c] = f[i][c]
                else:
                    f[i+1][c] = f[i][c] + f[i][c-x]

        return f[n][m]


