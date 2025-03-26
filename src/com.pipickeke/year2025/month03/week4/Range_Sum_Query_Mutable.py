from typing import List


"""
307. 区域和检索 - 数组可修改
给你一个数组 nums ，请你完成两类查询。

其中一类查询要求 更新 数组 nums 下标对应的值
另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right
实现 NumArray 类：

NumArray(int[] nums) 用整数数组 nums 初始化对象
void update(int index, int val) 将 nums[index] 的值 更新 为 val
int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]）

"""


class NumArray:
    __slots__ = 'nums','tree'

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.nums = [0] * n
        self.tree = [0] * (n+1)
        for i,x in enumerate(nums):
            self.update(i, x)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        i = index+1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i&-i

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum(right+1) - self.preSum(left)


    def preSum(self, index: int) -> int:
        s = 0
        while index:
            s += self.tree[index];
            index -= index&-index
        return s