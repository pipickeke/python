"""
1449. 数位成本和为目标值的最大数字


给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：

给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。
总成本必须恰好等于 target 。
添加的数位中没有数字 0 。
由于答案可能会很大，请你以字符串形式返回。

如果按照上述要求无法得到任何整数，请你返回 "0" 。


"""
from cmath import inf
from typing import List


class Solution:
    def largestNumber(self, cost:List[int], target:int)-> str:
        dp = [float('-inf')] * (target+1)
        dp[0] = 0

        for i in range(1,10):
            u = cost[i-1]
            for j in range(u, target+1):
                if dp[j-u] != float('-inf'):
                    dp[j] = max(dp[j], dp[j-u]+1)

        if dp[target] < 0:
            return "0"

        ans = []
        j = target
        for i in range(9, 0, -1):
            u = cost[i-1]
            while j >= u and dp[j] == dp[j-u]+1:
                ans.append(str(i))
                j -= u

        return "".join(ans)






    def largestNumber_2(self, cost:List[int], target:int)-> str:
        dp = [float('-inf')] * (target+1)
        dp[0] = 0

        for i in range(1,10):
            u = cost[i-1]
            for j in range(u, target+1):
                if dp[j-u] != float('-inf'):
                    dp[j] = max(dp[j], dp[j-u]+1)

        if dp[target] < 0:
            return "0"

        ans = []
        j = target
        for i in range(9,0,-1):
            u = cost[i-1]
            while j >= u and dp[j] == dp[j-u]+1:
                ans.append(str(i))
                j -= u

        return ''.join(ans)



