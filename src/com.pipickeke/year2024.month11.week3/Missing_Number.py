from typing import List

"""
    题目：丢失的数字
    给定一个包含 [0, n] 中 n 个数的数组 nums ，
    找出 [0, n] 这个范围内没有出现在数组中的那个数。
"""

def miss(nums: List[int]) -> int:
    tmp = 0
    for i, num in enumerate(nums):
        tmp ^= i ^ num
    tmp ^= len(nums)
    return tmp


if __name__ == '__main__':
    nums = [3,0,1]
    print(miss(nums))