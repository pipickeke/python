
"""
题目：数组中两个数的最大异或值

给你一个整数数组 nums ，返回 nums[i] XOR nums[j]
的最大运算结果，其中 0 ≤ i ≤ j < n 。


"""


def findMaximumXOR(nums):
    ans = mask = 0
    high_bit = max(nums).bit_length() - 1
    for i in range(high_bit, -1, -1):
        mask |= ( 1 << i)
        new_ans = ans | (1 <<i)
        seen = set()
        for x in nums:
            x = x & mask
            if new_ans ^ x in seen:
                ans = new_ans
                break
            seen.add(x)
    return ans
