from collections import defaultdict


"""
题目：1512. 好数对的数目

给你一个整数数组 nums 。

如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。

返回好数对的数目。

"""

def numIdenticalPairs(nums):
    ans = 0
    cnt = defaultdict(int)
    for x in nums:
        ans += cnt[x]
        cnt[x] += 1
    return ans





