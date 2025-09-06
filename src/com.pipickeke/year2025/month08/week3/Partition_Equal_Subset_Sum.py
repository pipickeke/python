"""
416. 分割等和子集
给你一个 只包含正整数 的 非空 数组 nums 。
请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

"""
from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> int:

        @cache
        def dfs(i: int, j: int) -> bool:
            if i < 0:
                return j == 0

            return j >= nums[i] and dfs(i-1, j-nums[i]) or dfs(i-1, j)

        s = sum(nums)
        return s % 2 == 0 and dfs(len(nums)-1, s // 2)


    def canPartition_2(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False

        s = s // 2
        n = len(nums)
        f = [[False] * (s+1) for _ in range(n+1)]
        f[0][0] = True
        for i, x in enumerate(nums):
            for j in range(s+1):
                f[i+1][j] = j >= x and f[i][j] or f[i][j-x]

        return f[n][s]





    def canPartition_3(self, nums: List[int]) -> bool:

        @cache
        def dfs(i: int, j: int) -> bool:
            if i < 0:
                return j == 0

            return j >= nums[i] and dfs(i-1, j-nums[i]) or dfs(i-1, j)

        s = sum(nums)

        return s % 2 == 0 and dfs(len(nums)-1, s // 2)




    def canPartition_4(self, nums: List[int]) -> int:
        s = sum(nums)
        if s % 2:
            return False

        n = len(nums)
        s = s // 2
        f = [[False] * (s+1) for _ in range(n+1)]
        f[0][0] = True
        for i, x in enumerate(nums):
            for j in range(s+1):
                f[i+1][j] = j >= x and f[i][j-x] or f[i][j]

        return f[n][s]



















