"""
3287. 求出数组中最大序列值

给你一个整数数组 nums 和一个 正 整数 k 。

定义长度为 2 * x 的序列 seq 的 值 为：

(seq[0] OR seq[1] OR ... OR seq[x - 1]) XOR (seq[x] OR seq[x + 1] OR ... OR seq[2 * x - 1]).
请你求出 nums 中所有长度为 2 * k 的 子序列 的 最大值 。


"""
from functools import reduce
from operator import or_
from typing import List


class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        mx = reduce(or_, nums)
        n = len(nums)
        suf = [None] * (n-k+1)
        f = [[False] * (mx+1) for _ in range(k+1)]
        f[0][0] = True

        for i in range(n-1, k-1, -1):
            v = nums[i]
            for j in range(min(k-1,n-1-i),-1,-1):
                for x, has_x in enumerate(f[j]):
                    if has_x:
                        f[j+1][x | v] = True

            if i <= n-k:
                suf[i] = f[k].copy()

        ans = 0
        f = [[False] * (mx+1) for _ in range(k+1)]
        f[0][0] = True
        for i,v in enumerate(nums[:-k]):
            for j in range(min(k-1,i),-1,-1):
                for x,has_x in enumerate(f[j]):
                    if has_x:
                        f[j+1][x|v] = True

            if i < k-1:
                continue

            for x, has_x in enumerate(f[k]):
                if has_x:
                    for y, has_y in enumerate(suf[i+1]):
                        if has_y and x ^ y > ans:
                            ans = x ^ y

            if ans == mx:
                return ans

        return ans



