"""
2902. 和带限制的子多重集合的数目

给你一个下标从 0 开始的非负整数数组 nums 和两个整数 l 和 r 。

请你返回 nums 中子多重集合的和在闭区间 [l, r] 之间的 子多重集合的数目 。

由于答案可能很大，请你将答案对 109 + 7 取余后返回。

子多重集合 指的是从数组中选出一些元素构成的 无序 集合，每个元素 x
出现的次数可以是 0, 1, ..., occ[x] 次，其中 occ[x] 是元素 x 在数组中的出现次数。

注意：

如果两个子多重集合中的元素排序后一模一样，那么它们两个是相同的 子多重集合 。
空 集合的和是 0 。



"""
from collections import Counter
from typing import List


class Solution:
    def countSubMultisets(self, nums:List[int],l:int,r:int)->int:
        MOD = int(1e9 + 7)
        total = sum(nums)
        if l > total:
            return 0

        r = min(total, r)
        cnt = Counter(nums)
        f = [cnt[0] + 1] + [0] * r
        del cnt[0]

        s = 0
        for x, c in cnt.items():
            s = min(s + x * c, r)
            new_f = f.copy()
            for j in range(x, s+1):
                new_f[j] += new_f[j-x]
                if j >= (c+1)*x:
                    new_f[j] -= f[j - (c+1)*x]
                new_f[j] %= MOD

            f = new_f

        return sum(f[l:]) % MOD






    def countSubMultisets_2(self, nums:List[int],l:int,r:int)->int:
        MOD = int(1e9 + 7)
        total = sum(nums)
        if l > total:
            return 0

        r = min(total,r)
        cnt = Counter(nums)
        f = [cnt[0] + 1] + [0]*r
        del cnt[0]

        s = 0
        for x,c in cnt.items():
            new_f = f.copy()
            s = min(s + x*c, r)
            for j in range(x, s+1):
                new_f[j] += new_f[j-x]
                if j >= (c+1)*x:
                    new_f[j] -= f[j - (c+1)*x]

                new_f[j] %= MOD

            f = new_f

        return sum(f[l:]) % MOD




