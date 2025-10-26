"""

518. 零钱兑换 II

给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。

请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。

假设每一种面额的硬币有无限个。

题目数据保证结果符合 32 位带符号整数。


"""
from functools import cache
from typing import List


class Solution:
    def change(self, amount:int, coins:List[int])->int:

        @cache
        def dfs(i, j):
            if i < 0:
                return 1 if j == 0 else 0
            if j < coins[i]:
                return dfs(i-1,j)

            ans = dfs(i-1, j) + dfs(i, j-coins[i])
            return ans

        return dfs(len(coins)-1, amount)





    def change_2(self, amount:int, coins:List[int])->int:
        dp = [[0] * (amount+1) for _ in range(len(coins)+1)]
        dp[0][0] = 1
        for i, x in enumerate(coins):
            for j in range(amount+1):
                if j < x:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = dp[i][j] + dp[i+1][j-x]
        return dp[-1][-1]


    def change_3(self, amount:int, coins:List[int])->int:
        dp = [1] + [0] * amount
        for x in coins:
            for j in range(x, amount+1):
                dp[j] = dp[j] + dp[j-x]

        return dp[-1]



