"""



"""
from math import inf
from typing import List


class Solution:
    def largestNumber(self, cost:List[int], target:int)->str:

        dp = [-inf] * (target+1)
        dp[0] = 0
        for i in range(1, 10):
            u = cost[i-1]
            for j in range(u, target+1):
                if dp[j-u] != -inf:
                    dp[j] = max(dp[j], dp[j-u]+1)

        if dp[target] < 0:
            return "0"

        ans = []
        j = target
        for i in range(9, 0, -1):
            u = cost[i-1]
            while j >= u and dp[j] == dp[j-u]+1:
                ans.append(str(i))
                j -= u
        return  "".join(ans)





    def largestNumber_2(self, cost:List[int], target:int)->str:
        dp = [-inf] * ( target + 1)
        dp[0] = 0

        for i in range(1, 10):
            u = cost[i-1]
            for j in range(u, target+1):
                if dp[j-u] != -inf:
                    dp[j] = max(dp[j], dp[j-u]+1)

        if dp[target] < 0:
            return "0"

        ans = []
        j = target
        for i in range(9, 0, -1):
            u = cost[i-1]
            while j >= u and dp[j] == dp[j-u]+1:
                ans.append(str(i))
                j -= u
        return "".join(ans)






