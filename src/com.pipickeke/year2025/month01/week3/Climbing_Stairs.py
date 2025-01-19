from functools import cache

"""
题目：70. 爬楼梯
标签：动态规划

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(i: int) -> int:
            if i < 2:
                return 1
            else:
                return dfs(i - 1) + dfs(i - 2)

        return dfs(n)

    def climbStairs2(self, n: int) -> int:
        f = [0] * (n + 1)
        f[0] = f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]


    def climbStairs3(self, n:int)->int:
        p = q = 1
        for i in range(2, n+1):
            tmp = p+q
            p = q
            q = tmp
        return q




