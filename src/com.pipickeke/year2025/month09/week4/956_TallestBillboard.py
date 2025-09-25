"""

956. 最高的广告牌


你正在安装一个广告牌，并希望它高度最大。这块广告牌将有两个钢制支架，
两边各一个。每个钢支架的高度必须相等。

你有一堆可以焊接在一起的钢筋 rods。举个例子，如果钢筋的长度为 1、2 和 3，
则可以将它们焊接在一起形成长度为 6 的支架。

返回 广告牌的最大可能安装高度 。如果没法安装广告牌，请返回 0 。


"""
from typing import List


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0:0}
        for i, x in enumerate(rods):
            for j,k in list(dp.items()):
                dp[j+x] = max(dp.get(j+x,0), k+x)
                dp[j-x] = max(dp.get(j-x,0), k)

        return dp[0]






    def tallestBillboard_2(self, rods: List[int]) -> int:
        dp = {0:0}
        for x in rods:
            for j,k in list(dp.items()):
                dp[j+x] = max(dp.get(j+x,0), k+x)
                dp[j-x] = max(dp.get(j-x,0), k)

        return dp[0]










