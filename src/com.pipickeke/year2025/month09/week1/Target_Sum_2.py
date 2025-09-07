"""


"""
from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self,nums:List[int],target:int)->int:
        n = len(nums)
        s = sum(nums) - abs(target)
        if s < 0 or s % 2:
            return 0

        m = (sum(nums)-abs(target)) // 2

        @cache
        def dfs(i, j):
            if i < 0:
                return 1 if j == 0 else 0

            if j < nums[i]:
                return dfs(i-1, j)

            return dfs(i-1, j) + dfs(i-1, j-nums[i])

        return dfs(n-1, m)


    def findTargetSumWays_2(self, nums: List[int], target:int)->int:
        s = sum(nums) - abs(target)
        if s < 0 or s % 2:
            return 0

        m = s // 2
        n = len(nums)
        f = [[0] * (m+1) for _ in range(n+1)]
        f[0][0] = 1

        for i, x in enumerate(nums):
            for c in range(m+1):
                if c < x:
                    f[i+1][c] = f[i][c]
                else:
                    f[i+1][c] = f[i][c] + f[i][c-x]

        return f[n][m]



    def findTargetSumWays_3(self, nums:List[int], target:int)->int:
        s = sum(nums) - abs(target)
        if s < 0 or s % 2:
            return 0

        m = s // 2
        f = [1] + [0]*m
        for x in nums:
            for c in range(m, x-1, -1):
                f[c] += f[c-x]

        return f[m]




