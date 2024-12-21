from functools import reduce
from operator import xor


def getMaximumXor(nums, maximumBit):
    n = len(nums)
    mask = (1 << maximumBit) - 1
    xorsum = reduce(xor, nums)

    ans = list()
    for i in range(n-1, -1, -1):
        ans.append(xorsum ^ mask)
        xorsum ^= nums[i]
    return  ans

