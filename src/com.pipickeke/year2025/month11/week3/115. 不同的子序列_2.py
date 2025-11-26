"""

115. 不同的子序列

给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数。

测试用例保证结果在 32 位有符号整数范围内。


"""
from functools import cache


class Solution:
    def numDistinct(self, s:str, t:str) -> int:

        @cache
        def dfs(i, j):
            if i < j:
                return 0

            if j < 0:
                return 1

            res = dfs(i-1, j)
            if s[i] == t[j]:
                res += dfs(i-1, j-1)
            return res

        return dfs(len(s)-1, len(t)-1)




    def numDistinct_2(self, s:str, t:str) -> int:
        m,n = len(s), len(t)

        dp = [[1] + [0] * n for _ in range(m+1)]

        for i, x in enumerate(s):
            for j in range(max(n-m+i,0), min(i+1, n)):
                dp[i+1][j+1] = dp[i][j+1]
                if x == t[j]:
                    dp[i+1][j+1] += dp[i][j]

        return dp[-1][-1]


    def numDistinct_3(self, s:str, t:str) -> int:
        n = len(t)
        m = len(s)

        dp = [1] + [0] * n
        for i, x in enumerate(s):
            for j in range(min(i, n-1), max(n-m+i, 0)-1, -1):
                if x == t[j]:
                    dp[j+1] += dp[j]

        return dp[-1]




