"""



"""
from typing import List


class Solution:
    def minZeroArray(self, nums:List[int], queries:List[List[int]])->int:

        ans = 0
        for i,x in enumerate(nums):
            if x == 0:
                continue

            f = [True] + [False]*x
            for j, (l,r,val) in enumerate(queries):
                if not l <= i <= r:
                    continue

                for k in range(x, val-1, -1):
                    f[k] = f[k] or f[k-val]

                if f[x]:
                    ans = max(ans, j+1)
                    break
            else:
                return -1

        return ans







