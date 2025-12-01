"""

2461. 长度为 K 子数组中的最大和

给你一个整数数组 nums 和一个整数 k 。请你从 nums 中满足下述条件的全部子数组中找出最大子数组和：

子数组的长度是 k，且
子数组中的所有元素 各不相同 。
返回满足题面要求的最大子数组和。如果不存在子数组满足这些条件，返回 0 。

子数组 是数组中一段连续非空的元素序列。

"""
from collections import defaultdict
from typing import List


class Solution:
    def maximumSubarraySum(self, nums:List[int], k:int) -> int:
        s = 0
        dt = defaultdict(int)
        ans = 0
        for i, x in enumerate(nums):
            s += x
            left = i-k+1
            dt[x] += 1

            if left < 0:
                continue

            if len(dt) == k:
                ans = max(ans, s)

            out = nums[left]
            s -= out
            dt[out] -= 1
            if dt[out] == 0:
                del dt[out]
        return ans






