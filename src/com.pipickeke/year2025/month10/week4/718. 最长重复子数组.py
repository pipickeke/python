"""



"""
from functools import cache
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int])->int:
        m, n = len(nums1), len(nums2)

        dp = [[0] * (n+1) for _ in range(m+1)]
        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                if x == y:
                    dp[i+1][j+1] = dp[i][j] + 1

        return max(map(max, dp))




    # OOM 报错
    def findLength_2(self, nums1: List[int], nums2: List[int])->int:
        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if nums1[i] == nums2[j]:
                return dfs(i-1, j-1) + 1
            else:
                return 0

        ans = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                ans = max(ans, dfs(i, j))

        return ans


