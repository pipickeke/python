

"""
题目：2275. 按位与结果大于零的最长组合

对数组 nums 执行 按位与 相当于对数组 nums 中的所有整数执行 按位与 。

例如，对 nums = [1, 5, 3] 来说，按位与等于 1 & 5 & 3 = 1 。
同样，对 nums = [7] 而言，按位与等于 7 。
给你一个正整数数组 candidates 。计算 candidates 中的数字每种组合下 按位与 的结果。

返回按位与结果大于 0 的 最长 组合的长度。


"""


def largestCombination(candidates):
    m = max(candidates).bit_length()
    return max(sum(x >> i & 1 for x in candidates) for i in range(m))