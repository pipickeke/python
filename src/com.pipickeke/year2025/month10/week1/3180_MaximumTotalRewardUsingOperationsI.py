"""

3180. 执行操作可获得的最大总奖励 I

给你一个整数数组 rewardValues，长度为 n，代表奖励的值。

最初，你的总奖励 x 为 0，所有下标都是 未标记 的。你可以执行以下操作 任意次 ：

从区间 [0, n - 1] 中选择一个 未标记 的下标 i。
如果 rewardValues[i] 大于 你当前的总奖励 x，则将 rewardValues[i]
加到 x 上（即 x = x + rewardValues[i]），并 标记 下标 i。
以整数形式返回执行最优操作能够获得的 最大 总奖励。


"""
from typing import List


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        maxval = rewardValues[-1]

        dp = [True] + [False] * (2*maxval)
        for i, x in enumerate(rewardValues):
            for j in range(x-1, -1, -1):
                if dp[j]:
                    dp[j+x] = True

        for i in range(2*maxval, -1, -1):
            if dp[i]:
                return i
        return 0








