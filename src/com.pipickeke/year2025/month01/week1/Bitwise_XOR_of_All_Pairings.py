from functools import reduce
from operator import xor

"""
题目：2425. 所有数对的异或和

给你两个下标从 0 开始的数组 nums1 和 nums2 ，两个数组都只包含非负整数。
请你求出另外一个数组 nums3 ，包含 nums1 和 nums2 中 所有数对 的异或和（nums1 中每个整数都跟 nums2 中每个整数 恰好 匹配一次）。

请你返回 nums3 中所有整数的 异或和 。

"""

def xorAllNums(nums1, nums2):
    M = len(nums1)
    N = len(nums2)
    ans = 0
    if N % 2:
        ans ^= reduce(xor, nums1)
    if M % 2:
        ans ^= reduce(xor, nums2)
    return ans