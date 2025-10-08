""""

279. 完全平方数


给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，
其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

"""
from math import isqrt, inf

N = 10000
dp = [[0] * (N+1) for _ in range(isqrt(N)+1)]
dp[0] = [0] + [inf] * N

for i in range(isqrt(N)+1):
    for j in range(N+1):
        if j < i * i:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = min(dp[i][j], dp[i+1][j- i*i] +1)





class Solution:
    def numSquares(self, n: int) -> int:
        return dp[isqrt(n)][n]