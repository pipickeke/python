

"""
题目：2411. 按位或最大的最小子数组长度

给你一个长度为 n 下标从 0 开始的数组 nums ，数组中所有数字均为非负整数。对于 0 到 n - 1 之间的每一个下标 i ，你需要找出 nums 中一个 最小 非空子数组，它的起始位置为 i （包含这个位置），同时有 最大 的 按位或运算值 。

换言之，令 Bij 表示子数组 nums[i...j] 的按位或运算的结果，你需要找到一个起始位置为 i 的最小子数组，这个子数组的按位或运算的结果等于 max(Bik) ，其中 i <= k <= n - 1 。
一个数组的按位或运算值是这个数组里所有数字按位或运算的结果。

请你返回一个大小为 n 的整数数组 answer，其中 answer[i]是开始位置为 i ，按位或运算结果最大，且 最短 子数组的长度。

子数组 是数组里一段连续非空元素组成的序列。

"""

def smallestSubarrays(nums):
    N = len(nums)
    ans = [0] * N
    for i,x in enumerate(nums):
        ans[i] = 1
        for j in range(i-1,-1,-1):
            if (nums[j] | nums[i]) == nums[j]:
                break
            nums[j] |= x
            ans[j] = i-j+1
    return ans