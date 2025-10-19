"""

1143. 最长公共子序列

给定两个字符串 text1 和 text2，返回这两个字符串的最长
公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字
符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。



"""
from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1:str, text2:str)->int:
        m,n = len(text1),len(text2)

        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0

            if text1[i] == text2[j]:
                return dfs(i-1,j-1)+1

            return max(dfs(i-1,j), dfs(i, j-1))

        return dfs(m-1, n-1)






    def longestCommonSubsequence_2(self, text1:str, text2:str)->int:
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]

        for i, x in enumerate(text1):
            for j, y in enumerate(text2):
                if x == y:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        return dp[-1][-1]







    def longestCommonSubsequence_3(self, text1:str, text2:str)->int:
        dp = [0] * (len(text2) + 1)
        for x in text1:
            pre = 0
            for j, y in enumerate(text2):
                tmp = dp[j+1]
                if x == y:
                    dp[j+1] = pre + 1
                else:
                    dp[j+1] = max(dp[j+1], dp[j])
                pre = tmp

        return dp[-1]





