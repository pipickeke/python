"""


"""
from cmath import inf
from typing import List


class Solution:
    def closestCost(self, baseCosts:List[int], toppingCosts:List[int],
                    target:int)->int:
        self.ans = 10**9
        for x in baseCosts:
            self.dfs(0, x, target, toppingCosts)
        return self.ans


    def dfs(self, idx, cur, target, toppingCosts):
        a = abs(target - cur)
        b = abs(target - self.ans)
        if a < b:
            self.ans = cur
        if a == b and cur < self.ans:
            self.ans = cur
        if cur > target:
            return

        for i in range(idx, len(toppingCosts)):
            self.dfs(i+1, cur+toppingCosts[i], target, toppingCosts)
            self.dfs(i+1, cur + 2*toppingCosts[i], target, toppingCosts)








