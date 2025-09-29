"""



"""
from typing import List


class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0] * (n+1) for _ in range(k+1)]
        dp[0][0] = 1
        MOD = int(1e9 + 7)

        for i, x in enumerate(nums):
            for j in range(k, x-1, -1):
                for c in range(i+1, 0, -1):
                    dp[j][c] = (dp[j][c] + dp[j-x][c-1]) %MOD

        ans = 0
        pow = 1
        for i in range(n, 0, -1):
            ans = (ans + dp[k][i] * pow) % MOD
            pow = pow * 2 % MOD

        return ans














