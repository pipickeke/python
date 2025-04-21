from bisect import bisect_left
from typing import List


"""
题目：3072. 将元素分配到两个数组中 II

给你一个下标从 1 开始、长度为 n 的整数数组 nums 。

现定义函数 greaterCount ，使得 greaterCount(arr, val) 返回数组 arr 中 严格大于 val 的元素数量。

你需要使用 n 次操作，将 nums 的所有元素分配到两个数组 arr1 和 arr2 中。在第一次操作中，将 nums[1] 追加到 arr1 。在第二次操作中，将 nums[2] 追加到 arr2 。之后，在第 i 次操作中：

如果 greaterCount(arr1, nums[i]) > greaterCount(arr2, nums[i]) ，将 nums[i] 追加到 arr1 。
如果 greaterCount(arr1, nums[i]) < greaterCount(arr2, nums[i]) ，将 nums[i] 追加到 arr2 。
如果 greaterCount(arr1, nums[i]) == greaterCount(arr2, nums[i]) ，将 nums[i] 追加到元素数量较少的数组中。
如果仍然相等，那么将 nums[i] 追加到 arr1 。
连接数组 arr1 和 arr2 形成数组 result 。例如，如果 arr1 == [1,2,3] 且 arr2 == [4,5,6] ，那么 result = [1,2,3,4,5,6] 。

返回整数数组 result 。


"""


class Solution:

    def resultArray(self, nums: List[int]) -> List[int]:
        sorted_arr = sorted(set(nums))
        m = len(sorted_arr)
        a = [nums[0]]
        b = [nums[1]]
        f1 = Fenwick(m+1)
        f2 = Fenwick(m+1)
        f1.add(bisect_left(sorted_arr, nums[0]) +1)
        f2.add(bisect_left(sorted_arr, nums[1]) +1)
        for x in nums[2:]:
            idx = bisect_left(sorted_arr, x) +1
            gc1 = len(a) - f1.pre(idx)
            gc2 = len(b) - f2.pre(idx)
            if gc1 > gc2 or gc1 == gc2 and len(a) <= len(b):
                a.append(x)
                f1.add(idx)
            else:
                b.append(x)
                f2.add(idx)

        return a+b




class Fenwick:
    __slots__ = 'tree'

    def __init__(self, n: int):
        self.tree = [0] * n

    def add(self, idx: int) -> None:
        while idx < len(self.tree):
            self.tree[idx]+=1
            idx += idx & -idx

    def pre(self, idx: int) -> int:
        ans = 0
        while idx > 0:
            ans += self.tree[idx]
            idx -= idx & -idx
        return ans




