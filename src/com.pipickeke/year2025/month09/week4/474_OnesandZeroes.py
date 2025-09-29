"""

474. 一和零

给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。


"""
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = [[0] * (n+1) for _ in range(m+1)]

        for i, x in enumerate(strs):
            cnt0 = x.count('0')
            cnt1 = len(x) - cnt0
            for j in range(m, cnt0-1, -1):
                for k in range(n, cnt1-1, -1):
                    dp[j][k] = max(dp[j][k], dp[j-cnt0][k-cnt1] + 1)

        return dp[m][n]






