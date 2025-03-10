from typing import List

"""
题目：152. 乘积最大子数组

给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 32-位 整数。

"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        fmax = [0]*n
        fmin = [0]*n
        fmax[0] = fmin[0] = nums[0]
        for i in range(1, n):
            x = nums[i]
            fmax[i] = max(x, max(fmax[i-1]*x, fmin[i-1]*x))
            fmin[i] = min(x, min(fmax[i-1]*x, fmin[i-1]*x))
        return max(fmax)