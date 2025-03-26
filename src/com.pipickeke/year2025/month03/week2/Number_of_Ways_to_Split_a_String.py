
"""
题目：1573. 分割字符串的方案数

给你一个二进制串 s  （一个只包含 0 和 1 的字符串），我们可以将 s 分割成 3 个 非空 字符串 s1, s2, s3 （s1 + s2 + s3 = s）。

请你返回分割 s 的方案数，满足 s1，s2 和 s3 中字符 '1' 的数目相同。

由于答案可能很大，请将它对 10^9 + 7 取余后返回。




"""

class Solution:
    def numWays(self,s: str) -> int:
        MOD = 1_000_000_007
        n = len(s)
        memo = list()
        for i,x in enumerate(s):
            if x == '1':
                memo.append(i)

        cnt = len(memo)
        if cnt % 3 != 0:
            return 0

        if cnt == 0:
            ans = ((n-1) * (n-2)) // 2
            return ans % MOD
        else:
            index1, index2 = cnt//3, cnt//3 * 2
            count1 = memo[index1] - memo[index1-1]
            count2 = memo[index2] - memo[index2-1]
            ans = count1 * count2
            return ans % MOD
