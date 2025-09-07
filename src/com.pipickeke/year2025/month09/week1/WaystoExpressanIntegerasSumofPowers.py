"""
2787. 将一个数字表示成幂的和的方案数

给你两个 正 整数 n 和 x 。

请你返回将 n 表示成一些 互不相同 正整数的 x 次幂之和的方案数。
换句话说，你需要返回互不相同整数 [n1, n2, ..., nk] 的集合数目，
满足 n = n1x + n2x + ... + nkx 。

由于答案可能非常大，请你将它对 109 + 7 取余后返回。

比方说，n = 160 且 x = 3 ，一个表示 n 的方法是 n = 23 + 33 + 53 。

"""

class Solution:
    def numberOfWays(self, n:int, x:int)->int:
        f = [1] + [0]*n
        for i in range(1,n+1):
            v = i ** x
            if v > n:
                break
            for s in range(n, v-1, -1):
                f[s] += f[s-v]

        return f[n] % 1_000_000_007


    def numberOfWays_2(self, n:int, x:int)->int:
        values = []
        for i in range(1,n+1):
            v = i ** x
            if v > n:
                break
            values.append(v)

        nums_value = len(values)
        f = [[0] * (n+1) for _ in range(nums_value+1)]
        f[0][0] = 1

        for i in range(1, nums_value+1):
            v = values[i-1]
            for s in range(n+1):
                f[i][s] = f[i-1][s]
                if s >= v:
                    f[i][s] += f[i-1][s-v]

        return f[nums_value][n] % 1_000_000_007




