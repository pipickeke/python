
"""
题目：238. 除自身以外数组的乘积

给你一个整数数组 nums，返回 数组 answer ，
其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请 不要使用除法，且在 O(n) 时间复杂度内完成此题。

"""


def productExceptSelf(nums):
    N = len(nums)
    pre = [1] * N
    for i in range(1,N):
        pre[i] = pre[i-1] * nums[i-1]

    suf = [1] * N
    for i in range(N-2,-1,-1):
        suf[i] = suf[i+1] * nums[i+1]
    return [p * s for p, s in zip(pre, suf)]