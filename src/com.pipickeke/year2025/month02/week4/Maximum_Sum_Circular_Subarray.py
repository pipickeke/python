from math import inf
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_s = -inf
        min_s = 0
        fmax = fmin = 0
        for x in nums:
            fmax = max(fmax,0) + x
            max_s = max(max_s, fmax)

            fmin = min(fmin,0) + x
            min_s = min(min_s, fmin)

        if sum(nums) == fmin:
            return max_s

        return max(max_s, sum(nums) - min_s)
