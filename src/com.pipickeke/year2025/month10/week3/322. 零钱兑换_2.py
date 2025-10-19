"""

322. 零钱兑换

给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。
如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。



"""
from functools import cache
from math import inf
from typing import List


class Solution:
    def coinChange(self, coins:List[int], amount:int)->int:

        @cache
        def dfs(i, j):
            if i < 0:
                return 0 if j == 0 else inf

            if j < coins[i]:
                return dfs(i-1, j)

            return min(dfs(i-1, j), dfs(i, j-coins[i])+1)

        ans = dfs(len(coins)-1, amount)

        return ans if ans < inf else -1




    def coinChange_2(self, coins:List[int], amount:int)->int:
        dp = [[inf] * (amount+1) for _ in range(len(coins)+1)]
        dp[0][0] = 0
        for i, x in enumerate(coins):
            for j in range(amount+1):
                if j < x:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = min(dp[i][j], dp[i+1][j-x]+1)

        ans = dp[len(coins)][amount]
        return ans if ans < inf else -1






