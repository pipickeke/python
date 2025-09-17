"""



"""
from typing import List


class Solution:
    def maxTotalReward(self, rewardValues:List[int])->int:
        rewardValues.sort()
        maxval = rewardValues[-1]

        f = [False] * (2*maxval+1)
        f[0] = True

        for x in rewardValues:
            for j in range(x-1, -1, -1):
                if f[j]:
                    f[j+x] = True

        for x in range(2*maxval,-1,-1):
            if f[x]:
                return x

        return 0



    def maxTotalReward_2(self, rewardValues: List[int]) -> int:
        rewardValues.sort()

        dp = 1
        for i, x in enumerate(rewardValues):
            mask = (1 << x) -1
            low_bit = dp & mask
            new_stat = low_bit << x
            dp |= new_stat

        if dp == 1:
            return 0

        return dp.bit_length()-1






