


"""
题目：2401. 最长优雅子数组

给你一个由 正 整数组成的数组 nums 。

如果 nums 的子数组中位于 不同 位置的每对元素按位
与（AND）运算的结果等于 0 ，则称该子数组为 优雅 子数组。

返回 最长 的优雅子数组的长度。

子数组 是数组中的一个 连续 部分。

注意：长度为 1 的子数组始终视作优雅子数组。

"""


def longestNiceSubarray(nums):
    ans = 0
    for i, or_ in enumerate(nums):
        j = i-1
        while j >=0 and (or_ & nums[j]) == 0:
            or_ |= nums[j]
            j -= 1
        ans = max(ans, i - j)
    return ans



def longestNiceSubarray_2(nums):
    ans = left = or_ = 0
    for right, x in enumerate(nums):
        while or_ & x :
            or_ ^= nums[left]
            left += 1
        or_ |= nums[right]
        ans = max(ans, right-left+1)
    return ans
