"""


"""
from typing import List

from numpy import sort


class Solution:
    def maxTotalReward(self,rewardValues:List[int])->int:
        rewardValues.sort()
        maxval = rewardValues[-1]
        dp = [False] * (2*maxval)
        dp[0] = True

        for val in rewardValues:
            for x in range(val-1,-1,-1):
                if dp[x]:
                    dp[x+val] = True

        for x in range(2*maxval-1, -1, -1):
            if dp[x]:
                return x
        return 0



    def maxTotalReward_2(self,rewardValues:List[int])->int:
        rewardValues.sort()
        maxval = rewardValues[-1]
        dp = [False] * (2*maxval)
        dp[0] = True

        for val in rewardValues:
            for x in range(val-1,-1,-1):
                if dp[x]:
                    dp[x+val] = True

        for x in range(2*maxval-1, -1,-1):
            if dp[x]:
                return x
        return 0


    def maxTotalReward_3(self,rewardValues:List[int])->int:
        rewardValues.sort()
        maxval = max(rewardValues)
        dp = 1

        pre = 0
        for val in rewardValues:
            if val == pre:
                continue

            mask = (1 << val) - 1
            lower_bit = dp & mask
            new_stat = lower_bit << val
            dp |= new_stat

        if dp == 1:
            return 0

        return dp.bit_length()-1




