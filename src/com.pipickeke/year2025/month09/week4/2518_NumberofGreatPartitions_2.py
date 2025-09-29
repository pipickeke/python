"""



"""
from typing import List


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums) < 2 * k: return 0
        n = len(nums)
        dp = [0] * k
        dp[0] = 1

        MOD = int(1e9 + 7)

        for i, x in enumerate(nums):
            for j in range(k-1, x-1, -1):
                dp[j] = (dp[j] + dp[j-x]) % MOD

        return (pow(2, n, MOD) - sum(dp) * 2) % MOD





    def countPartitions_2(self, nums: List[int], k: int) -> int:
        if sum(nums) < 2 * k : return 0
        dp = [0] * k
        dp[0] = 1

        MOD = int(1e9 + 7)

        for i, x in enumerate(nums):
            for j in range(k-1, x-1, -1):
                dp[j] = (dp[j] + dp[j-x]) % MOD

        return (pow(2, len(nums), MOD) - sum(dp) * 2) % MOD





