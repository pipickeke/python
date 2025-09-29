"""



"""
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        k = s - abs(target)
        if k < 0 or k % 2:
            return 0

        k = k // 2

        dp = [[0] * (k+1) for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for i, x in enumerate(nums):
            for j in range(k+1):
                if j < x:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = dp[i][j] + dp[i][j-x]

        return dp[len(nums)][k]



    def findTargetSumWays_2(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        k = sum(nums) - abs(target)
        if k < 0 or k % 2:
            return 0

        k = k // 2
        dp = [0] * (k+1)
        dp[0] = 1
        for i, x in enumerate(nums):
            for j in range(k, x-1, -1):
                dp[j] = dp[j] + dp[j-x]

        return dp[k]










