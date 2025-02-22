from itertools import accumulate
from typing import List

"""
题目：1749. 任意子数组和的绝对值的最大值

给你一个整数数组 nums 。一个子数组 [numsl, numsl+1, ..., numsr-1, numsr] 的 
和的绝对值 为 abs(numsl + numsl+1 + ... + numsr-1 + numsr) 。

请你找出 nums 中 和的绝对值 最大的任意子数组（可能为空），并返回该 最大值 。

abs(x) 定义如下：

如果 x 是负整数，那么 abs(x) = -x 。
如果 x 是非负整数，那么 abs(x) = x 。

"""

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = fmin = fmax = 0
        for x in nums:
            fmin = min(fmin, 0) + x
            fmax = max(fmax, 0) + x
            ans = max(ans, fmax, -fmin)
        return ans

    def maxAbsoluteSum_2(self, nums: List[int]) -> int:
        sum = mx = mn = 0
        for x in nums:
            sum += x
            if sum > mx:
                mx = sum
            elif sum < mn:
                mn = sum
        return mx - mn

    def maxAbsoluteSum_3(self, nums: List[int]) -> int:
        s = list(accumulate(nums, initial=0))
        return max(s) - min(s)
