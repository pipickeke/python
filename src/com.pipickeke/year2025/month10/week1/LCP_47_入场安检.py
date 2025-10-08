"""
LCP 47. 入场安检

「力扣挑战赛」 的入场仪式马上就要开始了，由于安保工作的需要，
设置了可容纳人数总和为 M 的 N 个安检室，capacities[i] 记录第 i 个安检室可容纳人数。
安检室拥有两种类型：

先进先出：在安检室中的所有观众中，最早进入安检室的观众最先离开
后进先出：在安检室中的所有观众中，最晚进入安检室的观众最先离开



"""
from typing import List


class Solution:
    def securityCheck(self, capacities: List[int], k: int) -> int:
        dp = [1] + [0] * k
        MOD = int(1e9 + 7)
        for x in capacities:
            x -= 1
            for y in range(k, x-1, -1):
                dp[y] = (dp[y] + dp[y-x]) % MOD

        return dp[k]