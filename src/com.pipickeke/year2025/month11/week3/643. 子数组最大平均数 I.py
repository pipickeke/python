"""

643. 子数组最大平均数 I

给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。

请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。

任何误差小于 10-5 的答案都将被视为正确答案。


"""
from cmath import inf
from typing import List


class Solution:
    def findMaxAverage(self, nums:List[int], k:int)->float:
        ans = sum = 0
        max_sum = -inf
        for i, x in enumerate(nums):
            sum += x
            left = i - k + 1
            if left < 0:
                continue

            max_sum = max(max_sum, sum)
            sum -= nums[left]

        return max_sum / k



    def findMaxAverage_2(self, nums:List[int], k:int)->float:
        sum = 0
        max_sum = -inf
        for i, x in enumerate(nums):
            sum += x
            left = i-k+1
            if left < 0:
                continue

            max_sum = max(max_sum, sum)
            sum -= nums[left]
        return max_sum / k





