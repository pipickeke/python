"""

474. 一和零


给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

"""
from functools import cache
from typing import List


class Solution:
    def findMaxForm(self,strs:List[str], m:int, n:int)->int:
        cnt0 = [str.count('0') for str in strs]

        @cache
        def dfs(i, j, k):
            if i < 0:
                return 0

            cnt1 = len(strs[i]) - cnt0[i]
            res = dfs(i-1, j, k)
            if j >= cnt0[i] and k >= cnt1:
                res = max(res, dfs(i-1, j - cnt0[i], k - cnt1) + 1)

            return res

        return dfs(len(strs)-1, m, n)



    def findMaxForm_2(self, strs: List[str], m: int, n: int) -> int:

        f = [[[0] * (n+1) for _ in range(m+1)] for _ in range(len(strs)+1)]
        for i, s in enumerate(strs):
            cnt0 = s.count('0')
            cnt1 = len(s)-cnt0
            for j in range(m+1):
                for k in range(n+1):
                    if j >= cnt0 and k >= cnt1:
                        f[i+1][j][k] = max(f[i][j][k], f[i][j-cnt0][k-cnt1]+1)
                    else:
                        f[i+1][j][k] = f[i][j][k]

        return f[-1][m][n]



    def findMaxForm_3(self, strs: List[str], m: int, n: int) -> int:

        f = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            cnt0 = s.count('0')
            cnt1 = len(s) - cnt0
            for j in range(m, cnt0-1, -1):
                for k in range(n, cnt1-1,-1):
                    if j >= cnt0 and k >= cnt1:
                        f[j][k] = max(f[j][k], f[j-cnt0][k-cnt1]+1)

        return f[m][n]











