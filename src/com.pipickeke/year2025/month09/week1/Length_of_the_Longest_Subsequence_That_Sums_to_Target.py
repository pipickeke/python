"""

2915. 和为目标值的最长子序列的长度

给你一个下标从 0 开始的整数数组 nums 和一个整数 target 。

返回和为 target 的 nums 子序列中，子序列 长度的最大值 。如果不存在和为 target 的子序列，返回 -1 。

子序列 指的是从原数组中删除一些或者不删除任何元素后，剩余元素保持原来的顺序构成的数组。
"""
from cmath import inf
from functools import cache
from typing import List


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int)->int:
        @cache
        def dfs(i, j):
            if i < 0:
                return 0 if j == 0 else -inf

            if nums[i] > j:
                return dfs(i-1, j)

            return max(dfs(i-1, j), dfs(i-1, j-nums[i]) + 1)

        ans = dfs(len(nums)-1, target)
        dfs.cache_clear()
        return ans if ans > 0 else -1


    def lengthOfLongestSubsequence_2(self, nums:List[int], target: int) -> int:
        n = len(nums)
        f = [[-inf] * (target+1) for _ in range(n+1)]
        f[0][0] = 0

        for i, x in enumerate(nums):
            for c in range(target+1):
                if x > c:
                    f[i+1][c] = f[i][c]
                else:
                    f[i+1][c] = max(f[i][c], f[i][c-x]+1)

        return f[n][target] if f[n][target] > 0 else -1


