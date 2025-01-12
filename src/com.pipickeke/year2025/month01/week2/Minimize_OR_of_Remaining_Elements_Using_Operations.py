

"""
题目：3022. 给定操作次数内使剩余元素的或值最小
标签：试填法

给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。

一次操作中，你可以选择 nums 中满足 0 <= i < nums.length - 1 的一个下标 i ，
并将 nums[i] 和 nums[i + 1] 替换为数字 nums[i] & nums[i + 1] ，其中 & 表示按位 AND 操作。

请你返回 至多 k 次操作以内，使 nums 中所有剩余元素按位 OR 结果的 最小值 。


"""



def minOrAfterOperations(nums, k):
    ans = mask = 0
    for i in range(max(nums).bit_length()-1,-1,-1):
        mask |= (1 << i)
        cnt = 0
        and_res = -1
        for x in nums:
            and_res &= x & mask
            if and_res:
                cnt += 1
            else:
                and_res = -1
        if cnt > k:
            ans |= (1 << i)
            mask ^= (1 <<i)
    return ans
