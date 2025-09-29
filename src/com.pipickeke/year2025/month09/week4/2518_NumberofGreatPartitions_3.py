"""

2518. 好分区的数目

给你一个正整数数组 nums 和一个整数 k 。

分区 的定义是：将数组划分成两个有序的 组 ，并满足每个元素 恰好 存在于 某一个 组中。如果分区中每个组的元素和都大于等于 k ，则认为分区是一个好分区。

返回 不同 的好分区的数目。由于答案可能很大，请返回对 109 + 7 取余 后的结果。

如果在两个分区中，存在某个元素 nums[i] 被分在不同的组中，则认为这两个分区不同。

"""
from typing import List


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums) < 2 * k: return 0
        dp = [0] * k
        dp[0] = 1
        MOD = int(1e9 + 7)
        for i, x in enumerate(nums):
            for j in range(k-1, x-1, -1):
                dp[j] = (dp[j] + dp[j-x]) % MOD

        return (pow(2,len(nums),MOD) - 2*sum(dp)) % MOD




    def countPartitions_2(self, nums: List[int], k: int) -> int:
        if sum(nums) < 2*k:
            return 0

        dp = [0] * k
        dp[0] = 1
        MOD = int(1e9 + 7)
        for i, x in enumerate(nums):
            for j in range(k-1, x-1, -1):
                dp[j] = (dp[j] + dp[j-x]) % MOD

        return (pow(2,len(nums),MOD) - 2*sum(dp)) % MOD




