from heapq import heapify, heapreplace
from typing import List

"""
题目：2208. 将数组和减半的最少操作次数

给你一个正整数数组 nums 。每一次操作中，你可以从 nums 中选择 任意 一个数并将它减小到 恰好 一半。（注意，在后续操作中你可以对减半过的数继续执行操作）

请你返回将 nums 数组和 至少 减少一半的 最少 操作数。


"""

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = -(nums[i] << 20)
        heapify(nums)
        ans = 0
        half = sum(nums) >> 1
        while half < 0:
            half -= nums[0] >> 1
            heapreplace(nums, nums[0] >> 1)
            ans += 1
        return ans
