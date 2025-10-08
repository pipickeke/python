"""



"""
from typing import List


class Solution:
    def findCoins(self, numWays:List[int])->List[int]:
        n = len(numWays)
        dp = [1] + [0]*n
        ans = []
        for i, x in enumerate(numWays,1):
            if x == dp[i]:
                continue

            if x-1 != dp[i]:
                return []

            ans.append(i)
            for j in range(i, n+1):
                dp[j] += dp[j-i]

        return ans





    def findCoins_2(self, numWays:List[int])->List[int]:
        n = len(numWays)
        dp = [1] + [0]*n
        ans = []
        for i, x in enumerate(numWays,1):
            if x == dp[i]:
                continue

            if x-1 != dp[i]:
                return []

            ans.append(i)
            for j in range(i, n+1):
                dp[j] += dp[j-i]

        return ans







