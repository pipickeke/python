"""

2585. 获得分数的方法数

考试中有 n 种类型的题目。给你一个整数 target 和一个下标从 0
开始的二维整数数组 types ，其中 types[i] = [counti, marksi]
表示第 i 种类型的题目有 counti 道，每道题目对应 marksi 分。

返回你在考试中恰好得到 target 分的方法数。由于答案可能很大，
结果需要对 109 +7 取余。

注意，同类型题目无法区分。

比如说，如果有 3 道同类型题目，那么解答第 1 和第 2 道题目与解答第 1
和第 3 道题目或者第 2 和第 3 道题目是相同的。


"""
from typing import List


class Solution:
    def waysToReachTarget(self, target:int, types: List[List[int]])->int:
        MOD = int(1e9 + 7)
        dp = [1] + [0]*target
        for count, mark in types:
            for i in range(target, mark-1, -1):
                for j in range(1, min(count, i // mark)+1):
                    dp[i] += dp[i - j*mark]

                dp[i] %= MOD

        return dp[-1]







