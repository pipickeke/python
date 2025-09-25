"""



"""
from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int)->int:
        self.ans = 10**9
        for x in baseCosts:
            self.dfs(0, x, target, toppingCosts)


        return self.ans

    def dfs(self, idx, cur, target, toppingCosts):
        a = abs(cur - target)
        b = abs(self.ans - target)
        if a < b:
            self.ans = cur

        if a == b and cur < self.ans:
            self.ans = cur

        if cur > target:
            return

        for i in range(idx, len(toppingCosts)):
            self.dfs(i+1, cur + toppingCosts[i], target, toppingCosts)
            self.dfs(i+1, cur + toppingCosts[i] * 2, target, toppingCosts)



