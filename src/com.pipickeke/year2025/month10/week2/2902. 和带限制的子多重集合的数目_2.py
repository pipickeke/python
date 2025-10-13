"""



"""
from collections import Counter
from typing import List


class Solution:
    def countSubMultisets(self, nums:List[int],l:int,r:int)->int:
        total = sum(nums)
        if l > total:
            return 0

        r = min(total,r)
        cnt = Counter(nums)
        MOD = int(1e9+ 7)
        f = [cnt[0] + 1] + [0]*r
        del cnt[0]

        s = 0
        for x, c in cnt.items():
            s = min(s + x*c, r)
            f_new = f.copy()
            for j in range(x, s+1):
                f_new[j] += f_new[j-x]
                if j >= (c+1)*x:
                    f_new[j] -= f[j - (c+1)*x]

                f_new[j] %= MOD

            f = f_new

        return sum(f[l:]) % MOD





