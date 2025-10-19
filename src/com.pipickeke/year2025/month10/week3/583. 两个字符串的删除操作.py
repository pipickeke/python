"""

583. 两个字符串的删除操作


给定两个单词 word1 和 word2 ，返回使得 word1 和  word2 相同所需的最小步数。

每步 可以删除任意一个字符串中的一个字符。


"""


class Solution:
    def minDistance(self, word1:str, word2:str)->int:
        m, n = len(word1), len(word2)

        dp = [[0] * (n+1) for _ in range(m+1)]
        for i, x in enumerate(word1):
            for j, y in enumerate(word2):
                if x == y:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        ans = dp[-1][-1]
        return m - ans + n - ans



