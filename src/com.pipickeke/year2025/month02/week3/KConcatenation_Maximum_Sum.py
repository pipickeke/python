from typing import List

"""
题目：1191. K 次串联后最大子数组之和

给定一个整数数组 arr 和一个整数 k ，通过重复 k 次来修改数组。

例如，如果 arr = [1, 2] ， k = 3 ，那么修改后的数组将是 [1, 2, 1, 2, 1, 2] 。

返回修改后的数组中的最大的子数组之和。注意，子数组长度可以是 0，在这种情况下它的总和也是 0。

由于 结果可能会很大，需要返回的 109 + 7 的 模 。

"""

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        a = arr * min(k, 2)
        ans = f = 0
        for _, x in enumerate(a):
            f = max(f, 0) + x
            ans = max(ans, f)

        s = sum(arr)
        if s > 0 and k > 2:
            ans = max(ans, s * (k-2) + ans)
        return ans % mod