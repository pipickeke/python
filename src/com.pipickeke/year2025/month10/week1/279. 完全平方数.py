"""

279. 完全平方数


给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；
换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。


"""
from functools import cache
from math import inf, isqrt


class Solution:
    def numSquares(self, n: int) -> int:

        @cache
        def dfs(i, j):
            if i == 0:
                return 0 if j == 0 else inf

            if j < i * i:
                return dfs(i-1, j)

            return min(dfs(i-1, j),
                       dfs(i, j - i * i)+1)

        return dfs(isqrt(n), n)


    def numSquares_2(self, n: int) -> int:
        return f[isqrt(n)][n]



N = 10000
f = [[0] * (N+1) for _ in range(isqrt(N)+1)]
f[0] = [0] + [inf] * N

for i in range(1, len(f)):
    for j in range(N+1):
        if j < i * i:
            f[i][j] = f[i-1][j]
        else:
            f[i][j] = min(f[i-1][j], f[i][j - i*i] + 1)






