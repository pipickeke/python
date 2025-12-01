"""

1423. 可获得的最大点数

几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。

每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。

你的点数就是你拿到手中的所有卡牌的点数之和。

给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。


"""
from math import inf
from typing import List


class Solution:
    def maxScore(self, cardPoints:List[int], k:int) -> int:
        n = len(cardPoints)
        m = n-k
        s = min_s = sum(cardPoints[:m])
        for i in range(m, n):
            s += cardPoints[i] - cardPoints[i-m]
            min_s = min(min_s, s)
        return sum(cardPoints) - min_s








    def maxScore_2(self, cardPoints:List[int], k:int) -> int:
        n = len(cardPoints)
        m = n-k
        s = min_s = sum(cardPoints[:m])
        for i in range(m,n):
            s += cardPoints[i] - cardPoints[i-m]
            min_s = min(min_s, s)
        return sum(cardPoints) - min_s

