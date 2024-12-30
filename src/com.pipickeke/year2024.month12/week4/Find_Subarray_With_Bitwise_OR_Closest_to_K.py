from cmath import inf


"""
题目：3171. 找到按位或最接近 K 的子数组

给你一个数组 nums 和一个整数 k 。你需要找到 nums 的一个 
子数组
 ，满足子数组中所有元素按位或运算 OR 的值与 k 的 绝对差 尽可能 小 。
 换言之，你需要选择一个子数组 nums[l..r] 满足 |k - (nums[l] OR nums[l + 1] ... OR nums[r])| 最小。

请你返回 最小 的绝对差值。

子数组 是数组中连续的 非空 元素序列。
"""

def minimumDifference(nums, k):
    ans = inf
    for i, x  in enumerate(nums):
        ans = min(ans, abs(x-k))
        j = i - 1
        while j>=0 and nums[j] | x != nums[j]:
            nums[j] |= x
            ans = min(ans, abs(nums[j] - k))
            j -= 1
    return ans

