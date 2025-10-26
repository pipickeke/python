"""

1458. 两个子序列的最大点积

给你两个数组 nums1 和 nums2 。

请你返回 nums1 和 nums2 中两个长度相同的 非空 子序列的最大点积。

数组的非空子序列是通过删除原数组中某些元素（可能一个也不删除）
后剩余数字组成的序列，但不能改变数字间相对顺序。比方说，[2,3,5]
是 [1,2,3,4,5] 的一个子序列而 [1,5,3] 不是。




"""
from functools import cache
from math import inf
from typing import List


class Solution:
    def maxDotProduct(self, nums1:List[int], nums2:List[int])->int:
        m,n = len(nums1), len(nums2)

        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return -inf
            cur = nums1[i] * nums2[j]
            return max(
                dfs(i-1, j-1) + cur,
                cur,
                dfs(i-1, j),
                dfs(i, j-1)
            )
        return dfs(m-1, n-1)





    def maxDotProduct_2(self, nums1:List[int], nums2:List[int])->int:
        m,n = len(nums1), len(nums2)
        dp = [[-inf] * (n+1) for _ in range(m+1)]
        dp[0][0] = 0
        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                cur = x*y
                dp[i+1][j+1] = max(dp[i][j]+cur,
                                   cur,
                                   dp[i+1][j],
                                   dp[i][j+1])
        return dp[-1][-1]





