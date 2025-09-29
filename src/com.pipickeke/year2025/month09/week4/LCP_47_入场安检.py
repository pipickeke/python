"""


"""
from typing import List


class Solution:
    def securityCheck(self, capacities: List[int], k: int) -> int:
        dp = [1] + [0] * k
        for i, x in enumerate(capacities):
            x -= 1
            for j in range(k, x-1, -1):
                dp[j] = (dp[j] + dp[j-x]) % int(1e9 + 7)

        return dp[k]






