"""

712. 两个字符串的最小ASCII删除和

给定两个字符串s1 和 s2，返回 使两个字符串相等所需删除字符的 ASCII 值的最小和 。





"""


class Solution:
    def minimumDeleteSum(self, s1:str, s2:str)->int:
        m,n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i, x in enumerate(s1):
            for j, y in enumerate(s2):
                if x == y:
                    dp[i+1][j+1] = dp[i][j] + ord(x)
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        ascii_s1 = sum(ord(c) for c in s1)
        ascii_s2 = sum(ord(c) for c in s2)
        res = ascii_s1 - dp[-1][-1] + ascii_s2 - dp[-1][-1]
        return res









