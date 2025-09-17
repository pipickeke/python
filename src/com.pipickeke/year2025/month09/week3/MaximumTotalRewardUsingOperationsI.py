"""



"""
from typing import List


class Solution:
    def maxTotalReward(self, rewardValues: List[int])->int:
        rewardValues.sort()
        maxval = rewardValues[-1]

        f = [False] * (2*maxval+1)
        f[0] = True

        for val in rewardValues:
            for c in range(val-1, -1, -1):
                if f[c]:
                    f[c+val] = True

        for s in range(2*maxval,-1,-1):
            if f[s]:
                return s
        return 0


    def maxTotalReward_2(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        dp = 1

        for val in rewardValues:
            mask = (1 << val) - 1
            low_bit = dp & mask
            new_stat = low_bit << val
            dp |= new_stat

        if dp == 1:
            return 0

        return dp.bit_length()-1






