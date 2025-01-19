from functools import cache
from typing import List

"""
题目：746. 使用最小花费爬楼梯
标签：动态规划

给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

请你计算并返回达到楼梯顶部的最低花费。

"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(n: int) -> int:
            if n <= 1:
                return 0
            return min(dfs(n - 1) + cost[n - 1], dfs(n - 2) + cost[n - 2])

        return dfs(len(cost))

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        @cache
        def dfs(n: int) -> int:
            if n <= 1:
                return 0
            return min(dfs(n - 1) + cost[n - 1], dfs(n - 2) + cost[n - 2])

        return dfs(len(cost))

    def minCostClimbingStairs3(self, cost: List[int]) -> int:
        n = len(cost)
        ans = [0] * (n+1)
        ans[0] = ans[1] = 0
        for i in range(2, n+1):
            ans[i] = min(ans[i-1]+cost[i-1],
                         ans[i-2]+cost[i-2])
        return ans[n]











