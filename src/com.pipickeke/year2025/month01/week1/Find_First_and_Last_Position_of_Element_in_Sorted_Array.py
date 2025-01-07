from typing import List

"""
题目：34. 在排序数组中查找元素的第一个和最后一个位置
标签：二分查找

给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。
请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

"""


class Solution:

    def lowbound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            # nums[left-1] < target
            # nums[right+1] >= target
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left


    def searchRange(self, nums: List[int], target: int) -> int:

        start = self.lowbound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = self.lowbound(nums, target + 1) - 1
        return [start, end]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    bean = Solution()
    print(bean.searchRange(nums, target))