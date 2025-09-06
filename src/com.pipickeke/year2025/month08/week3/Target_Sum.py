"""
494. 目标和
给你一个非负整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

"""
from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return 1 if j == 0 else 0

            return dfs(i-1, j-nums[i]) + dfs(i-1, j+nums[i])

        n = len(nums)
        return dfs(n-1, target)


    def findTargetSumWays_2(self, nums: List[int], target: int) -> int:
        s = sum(nums) - abs(target)
        if s < 0 or s % 2:
            return 0






