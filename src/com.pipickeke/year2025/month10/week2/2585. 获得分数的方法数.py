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
    def waysToReachTarget(self,target:int,types:List[List[int]])->int:
        f = [1] + [0] * target
        MOD = int(1e9 + 7)
        for cnt,mark in types:
            for j in range(target, mark-1, -1):
                for k in range(1, min(cnt, j // mark)+1):
                    f[j] += f[j - k * mark]

                f[j] %= MOD

        return f[target]



