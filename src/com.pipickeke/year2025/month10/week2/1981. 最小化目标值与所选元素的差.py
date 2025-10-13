"""

1981. 最小化目标值与所选元素的差

给你一个大小为 m x n 的整数矩阵 mat 和一个整数 target 。

从矩阵的 每一行 中选择一个整数，你的目标是 最小化 所有选中元素之
 和 与目标值 target 的 绝对差 。

返回 最小的绝对差 。

a 和 b 两数字的 绝对差 是 a - b 的绝对值


"""
from typing import List


class Solution:
    def minimizeTheDifference(self, mat:List[List[int]], target):
        max_possible = min(len(mat)*70, target * 2)
        dp = [False] * (max_possible+1)
        dp[0] = True

        min_sum = 0
        max_sum = 0
        for row in mat:
            mi = min(row)
            mx = max(row)

            min_sum += mi
            max_sum = min(max_sum + mx, target * 2)


            new_dp = [False] * (max_possible + 1)
            for j in range(max_possible + 1):
                for v in row:
                    if v <= j and dp[j-v]:
                        new_dp[j] = True
                        break

            dp = new_dp

        ans = abs(min_sum - target)
        for i, c in enumerate(dp):
            if c:
                ans = min(ans, abs(i - target))

        return ans











    def minimizeTheDifference_2(self, mat:List[List[int]], target):
        max_possible = min(len(mat)*70, target*2)
        dp = [False] * (max_possible+1)
        dp[0] = True

        min_sum = 0
        max_sum = 0
        for row in mat:
            mi = min(row)
            mx = max(row)

            min_sum += mi
            max_sum = min(max_sum + mx, target * 2)

            new_dp = [False] * (max_possible + 1)
            for j in range(max_possible+1):
                for v in row:
                    if j >= v and dp[j-v]:
                        new_dp[j] = True
                        break
            dp = new_dp

        ans = abs(min_sum - target)
        for i, c in enumerate(dp):
            if c:
                ans = min(ans, abs(i - target))

        return ans















    def minimizeTheDifference_3(self, mat:List[List[int]], target):
        max_possible = target*2
        dp = [True] + [False] * max_possible
        min_sum = 0
        max_sum = 0

        for row in mat:
            mi = min(row)
            mx = max(row)

            min_sum += mi
            max_sum = min(max_sum + mx, target*2)

            new_dp = [False] * (max_possible+1)
            for j in range(max_possible+1):
                for v in row:
                    if j >= v and dp[j-v]:
                        new_dp[j] = True
                        break

            dp = new_dp

        ans = abs(min_sum - target)
        for i, c in enumerate(dp):
            if c:
                ans = min(ans, abs(i - target))

        return ans









