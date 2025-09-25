"""
879. 盈利计划


集团里有 n 名员工，他们可以完成各种各样的工作创造利润。

第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。
如果成员参与了其中一项工作，就不能参与另一项工作。

工作的任何至少产生 minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。

有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。


"""
from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = int(1e9+7)
        m = len(group)

        f = [[[0] * (minProfit+1) for _ in range(n+1)] for _ in range(m+1)]
        for i in range(n+1):
            f[0][i][0] = 1

        for i in range(1, m+1):
            g = group[i-1]
            p = profit[i-1]
            for j in range(n+1):
                for k in range(minProfit+1):
                    f[i][j][k] = f[i-1][j][k]
                    if j >= g:
                        pre_profit = max(k-p, 0)
                        f[i][j][k] += f[i-1][j-g][pre_profit]
                        if f[i][j][k] >= mod:
                            f[i][j][k] -= mod

        return f[m][n][minProfit]
