from functools import cache
from typing import List



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dfs(x: int) -> int:
            res = 0
            for j in range(x):
                if nums[j] < nums[x]:
                    res = max(res, dfs(j))
            return ++res

        return max(dfs(i) for i in range(len(nums)))


    def lengthOfLIS_2(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        ans = 0
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j])
            ans = max(ans, ++dp[i])

        return ans







