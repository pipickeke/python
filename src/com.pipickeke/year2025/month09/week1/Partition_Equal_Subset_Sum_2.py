"""
416. 分割等和子集

给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两
个子集，使得两个子集的元素和相等。

"""
from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums:List[int])->bool:
        s = sum(nums)
        if s % 2 != 0:
            return False

        @cache
        def dfs(i, j):
            if i < 0:
                return j == 0

            if j < nums[i]:
                return dfs(i-1, j)

            return dfs(i-1, j) or dfs(i-1, j-nums[i])

        m = s // 2
        return dfs(len(nums)-1, m)


    def canPartition_2(self, nums: List[int])->bool:
        n = len(nums)
        s = sum(nums)

        if s % 2 != 0:
            return False

        m = s // 2
        f = [[False] * (m+1) for _ in range(n+1)]
        f[0][0] = True
        for i, x in enumerate(nums):
            for c in range(m+1):
                if c < x:
                    f[i+1][c] = f[i][c]
                else:
                    f[i+1][c] = f[i][c] or f[i][c-x]

        return f[n][m]
