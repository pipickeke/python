"""

3290. 最高乘法得分

给你一个大小为 4 的整数数组 a 和一个大小 至少为 4 的整数数组 b。

你需要从数组 b 中选择四个下标 i0, i1, i2, 和 i3，
并满足 i0 < i1 < i2 < i3。你的得分将是 a[0] * b[i0] + a[1] * b[i1] + a[2] * b[i2] + a[3] * b[i3] 的值。

返回你能够获得的 最大 得分。


"""
from functools import cache
from math import inf
from typing import List


class Solution:
    def maxScore(self, a:List[int], b:List[int])->int:

        @cache
        def dfs(i, j):
            if j < 0:
                return 0
            if i < 0:
                return -inf
            return max(
                dfs(i-1, j),
                dfs(i-1, j-1) + a[j] * b[i]
            )

        ans = dfs(len(b)-1, 3)
        dfs.cache_clear()
        return ans


    def maxScore_2(self, a:List[int], b:List[int])->int:
        dp = [[0] * 5 for _ in range(len(b)+1)]
        dp[0][1:] = [-inf] * 4

        for i, x in enumerate(b):
            for j, y in enumerate(a):
                dp[i+1][j+1] = max(
                    dp[i][j+1],
                    dp[i][j] + y * x
                )

        return dp[-1][-1]



    def maxScore_3(self, a:List[int], b:List[int])->int:
        f = [0] + [-inf] * 4

        for y in b:
            for j in range(3,-1,-1):
                f[j+1] = max(f[j+1], f[j] + y * a[j])

        return f[-1]




    def maxScore_4(self, a:List[int], b:List[int])->int:
        dp = [0] + [-inf]*4

        for x in b:
            for j in range(3,-1,-1):
                dp[j+1] = max(dp[j+1],dp[j] + x * a[j])

        return dp[-1]
