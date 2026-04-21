"""
3652. 按策略买卖股票的最佳时机

给你两个整数数组 prices 和 strategy，其中：

prices[i] 表示第 i 天某股票的价格。
strategy[i] 表示第 i 天的交易策略，其中：
-1 表示买入一单位股票。
0 表示持有股票。
1 表示卖出一单位股票。
同时给你一个 偶数 整数 k，你可以对 strategy 进行 最多一次 修改。一次修改包括：

选择 strategy 中恰好 k 个 连续 元素。
将前 k / 2 个元素设为 0（持有）。
将后 k / 2 个元素设为 1（卖出）。
利润 定义为所有天数中 strategy[i] * prices[i] 的 总和 。

返回你可以获得的 最大 可能利润。

注意： 没有预算或股票持有数量的限制，因此所有买入和卖出操作均可行，无需考虑过去的操作。


"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy:List[int], k:int)->int:
        total = max_s = s = 0
        for i, (p, st) in enumerate(zip(prices, strategy)):
            total += p*st
            s += p * (1 - st)


            if i < k-1:
                if i >= k // 2 - 1:
                    s -= prices[i - k// 2 + 1]
                continue

            max_s = max(max_s, s)
            s -= prices[i - k//2 + 1] - prices[i-k+1] * strategy[i-k+1]
        return total + max_s









