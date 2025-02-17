from collections import Counter
from typing import List

"""
题目：740. 删除并获得点数

给你一个整数数组 nums ，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。
之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

"""

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        nums.sort()
        nums = list(set(nums))
        n = nums[-1]
        dp = [0, cnt[1]]
        for i in range(2, n+1):
            dp[0], dp[1] = dp[1], max(dp[1], dp[0] + i*cnt[i])
        return dp[1]

