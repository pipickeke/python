"""

718. 最长重复子数组


给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。




"""
from functools import cache
from typing import List


class Solution:

    ### OOM
    def findLength(self, nums1:List[int], nums2:List[int])->int:
        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if nums1[i] == nums2[j]:
                return dfs(i-1, j-1)+1
            else:
                return 0

        ans = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                ans = max(ans, dfs(i,j))
        return ans





    def findLength_2(self, nums1:List[int], nums2:List[int])->int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                if x == y:
                    dp[i+1][j+1] = dp[i][j] +1
                else:
                    dp[i+1][j+1] = 0
        return max(map(max, dp))








