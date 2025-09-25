"""
3082. 求出所有子序列的能量和


给你一个长度为 n 的整数数组 nums 和一个 正 整数 k 。

一个整数数组的 能量 定义为和 等于 k 的子序列的数目。

请你返回 nums 中所有子序列的 能量和 。

由于答案可能很大，请你将它对 109 + 7 取余 后返回


"""
from typing import List


class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [[0] * (n+1) for _ in range(k+1)]
        f[0][0] = 1

        mod = int(1e9 + 7)
        for i,x in enumerate(nums):
            for j in range(k, x-1,-1):
                for c in range(i+1,0,-1):
                    f[j][c] = (f[j][c] + f[j-x][c-1]) % mod

        ans = 0
        pow = 1
        for i in range(n,0,-1):
            ans = (ans + f[k][i] * pow) % mod
            pow = pow * 2 % mod

        return ans




    def sumOfPower_2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [[0] * (n+1) for _ in range(k+1)]
        f[0][0] = 1
        mod = int(1e9+7)

        for i, x in enumerate(nums):
            for j in range(k, x-1, -1):
                for c in range(i+1, 0, -1):
                    f[j][c] = (f[j][c] + f[j-x][c-1]) %mod

        ans = 0
        pow = 1
        for i in range(n, 0, -1):
            ans = (ans + f[k][i] * pow) % mod
            pow = pow * 2 % mod

        return ans






    def sumOfPower_3(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MOD = int(1e9 + 7)
        f = [[0] * (n+1) for _ in range(k+1)]
        f[0][0] = 1

        for i, x in enumerate(nums):
            for j in range(k, x-1, -1):
                for c in range(i+1, 0, -1):
                    f[j][c] = f[j][c] + f[j-x][c-1]

        ans = 0
        pow = 1
        for i in range(n, 0, -1):
            ans = (ans + f[k][i] * pow) % MOD
            pow = pow * 2 % MOD

        return ans



