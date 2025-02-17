from collections import Counter
from functools import cache
from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]):
        cnt = Counter(power)
        a = sorted(cnt.keys())

        @cache
        def dfs(i: int):
            if i < 0:
                return 0
            x = a[i]
            j = i
            while j and a[j - 1] >= x - 2:
                j -= 1
            return max(dfs(i - 1), dfs(j - 1) + cnt[x] * x)

        return dfs(len(a) - 1)
