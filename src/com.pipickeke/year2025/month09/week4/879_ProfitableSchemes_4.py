"""

879. 盈利计划

集团里有 n 名员工，他们可以完成各种各样的工作创造利润。

第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。

工作的任何至少产生 minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。

有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。

"""
from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m = len(group)
        dp = [[[0] * (minProfit+1) for _ in range(n+1)] for _ in range(m+1)]
        for i in range(n+1):
            dp[0][i][0] = 1

        MOD = int(1e9 + 7)
        for i in range(m):
            for j in range(n+1):
                for k in range(minProfit+1):
                    dp[i+1][j][k] = dp[i][j][k]
                    if j >= group[i]:
                        dp[i+1][j][k] += dp[i][j-group[i]][max(k-profit[i], 0)]
                        dp[i+1][j][k] %= MOD

        return dp[m][n][minProfit]

