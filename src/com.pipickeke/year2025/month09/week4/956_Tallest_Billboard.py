"""



"""
from typing import List


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0:0}

        for x in rods:
            for k,v in list(dp.items()):
                dp[k+x] = max(dp.get(k+x, 0), v+x)
                dp[k-x] = max(dp.get(k-x, 0), v)

        return dp[0]








