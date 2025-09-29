"""



"""
from typing import List


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0] * (k+1) for _ in range(n+1)]
        dp[0][0] = 1

        MOD = int(1e9 + 7)

        for i,x in enumerate(nums):
            for j in range(k+1):
                if j < x:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = (dp[i][j] + dp[i][j-x]) % MOD

        ans = 0
        for i in range(k+1):
            ans += dp[n][i]

        return ( pow(2, len(nums), MOD) - ans*2 ) %MOD





    def countPartitions_2(self, nums: List[int], k: int) -> int:
        if sum(nums) < k * 2: return 0
        n = len(nums)
        dp = [0] * k
        dp[0] = 1

        MOD = int(1e9 + 7)

        for i, x in enumerate(nums):
            for j in range(k-1, x-1, -1):
                dp[j] = (dp[j] + dp[j-x]) % MOD

        return ( pow(2, len(nums), MOD) - sum(dp)*2 ) % MOD


