"""

2218. 从栈中取出 K 个硬币的最大面值和

一张桌子上总共有 n 个硬币 栈 。每个栈有 正整数 个带面值的硬币。

每一次操作中，你可以从任意一个栈的 顶部 取出 1 个硬币，从栈中移除它，并放入你的钱包里。

给你一个列表 piles ，其中 piles[i] 是一个整数数组，分别表示第 i
个栈里 从顶到底 的硬币面值。同时给你一个正整数 k ，请你返回在 恰好
进行 k 次操作的前提下，你钱包里硬币面值之和 最大为多少 。



"""
from itertools import accumulate
from typing import List


class Solution:
    def maxValueOfCoins(self, piles:List[List[int]], k:int)->int:
        dp = [[0] * (k+1) for _ in range(len(piles)+1)]

        for i, row in enumerate(piles):
            for j in range(k+1):
                dp[i+1][j] = dp[i][j]
                for w,v in enumerate(accumulate(row[:j]), 1):
                    dp[i+1][j] = max(dp[i+1][j], dp[i][j-w]+v)

        return dp[-1][k]







