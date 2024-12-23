

"""
题目：2871. 将数组分割成最多数目的子数组

给你一个只包含 非负 整数的数组 nums 。

我们定义满足 l <= r 的子数组 nums[l..r] 的分数为 nums[l] AND nums[l + 1] AND ... AND nums[r] ，其中 AND 是按位与运算。

请你将数组分割成一个或者更多子数组，满足：

每个 元素都 只 属于一个子数组。
子数组分数之和尽可能 小 。
请你在满足以上要求的条件下，返回 最多 可以得到多少个子数组。

一个 子数组 是一个数组中一段连续的元素。

"""


def maxSubarrays(nums):
    mask = -1
    ans = 0
    for x in nums:
        mask &= x
        if mask == 0:
            ans += 1
            mask = -1
    return max(ans, 1)






