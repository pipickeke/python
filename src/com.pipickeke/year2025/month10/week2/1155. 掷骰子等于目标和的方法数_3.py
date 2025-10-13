"""
1155. 掷骰子等于目标和的方法数

这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。

给定三个整数 n、k 和 target，请返回投掷骰子的所有可能得到的结果
（共有 kn 种方式），使得骰子面朝上的数字总和等于 target。

由于答案可能很大，你需要对 109 + 7 取模。


"""
from functools import cache


class Solution:
    def numRollsToTarget(self, n:int, k:int, target:int)->int:
        MOD = int(1e9 + 7)

        @cache
        def dfs(i, j):
            if j < 0:
                return 0
            if i <= 0:
                return int(j == 0)

            ans = 0
            for x in range(1,k+1):
                ans += dfs(i-1, j-x)
            return ans % MOD

        return dfs(n, target)


    def numRollsToTarget_2(self, n:int, k:int, target:int)->int:
        MOD = int(1e9 + 7)
        dp = [[0] * (target-n+1) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(1,n+1):
            for j in range(target-n+1):
                for x in range(min(k, j+1)):
                    dp[i][j] = (dp[i][j] + dp[i-1][j-x]) % MOD

        return dp[n][-1]









