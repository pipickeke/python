"""

1035. 不相交的线

在两条独立的水平线上按给定的顺序写下 nums1 和 nums2 中的整数。

现在，可以绘制一些连接两个数字 nums1[i] 和 nums2[j] 的直线，这些直线需要同时满足：

 nums1[i] == nums2[j]
且绘制的直线不与任何其他连线（非水平线）相交。
请注意，连线即使在端点也不能相交：每个数字只能属于一条连线。

以这种方法绘制线条，并返回可以绘制的最大连线数。


"""
from functools import cache
from typing import List


class Solution:
    def maxUncrossedLines(self, nums1:List[int], nums2:List[int])->int:
        m,n = len(nums1), len(nums2)
        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if nums1[i] == nums2[j]:
                return dfs(i-1, j-1)+1
            return max(dfs(i-1, j), dfs(i, j-1))
        return dfs(m-1, n-1)


    def maxUncrossedLines_2(self, nums1:List[int], nums2:List[int])->int:
        m,n = len(nums1), len(nums2)

        dp = [[0] * (n+1) for _ in range(m+1)]
        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                if x == y:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        return dp[-1][-1]




    def maxUncrossedLines_3(self, nums1:List[int], nums2:List[int])->int:
        dp = [0] * (len(nums2)+1)
        for i, x in enumerate(nums1):
            pre = 0
            for j, y in enumerate(nums2):
                tmp = dp[j+1]
                dp[j+1] = pre+1 if x == y else max(dp[j], dp[j+1])
                pre = tmp

        return dp[-1]





    def maxUncrossedLines_4(self, nums1:List[int], nums2:List[int])->int:
        dp = [0] * (len(nums2)+1)
        for i, x in enumerate(nums1):
            pre = 0
            for j, y in enumerate(nums2):
                tmp = dp[j+1]
                dp[j+1] = pre+1 if x == y else max(dp[j], dp[j+1])
                pre = tmp
        return dp[-1]





