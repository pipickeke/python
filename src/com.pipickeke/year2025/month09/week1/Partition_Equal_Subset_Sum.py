"""
416. 分割等和子集
给你一个 只包含正整数 的 非空 数组 nums 。
请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

"""
from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        @cache
        def dfs(i, j):
            if i < 0:
                return j == 0

            if j < nums[i]:
                return dfs(i-1, j)

            return dfs(i-1, j-nums[i]) or dfs(i-1, j)

        return dfs(len(nums)-1, sum(nums)//2)




