"""

72. 编辑距离

给你两个单词 word1 和 word2， 请返回将 word1
转换成 word2 所使用的最少操作数  。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符


"""
from functools import cache


class Solution:
    def minDistance(self, word1:str, word2:str)->int:

        @cache
        def dfs(i, j):
            if i < 0:
                return j+1
            if j < 0:
                return i+1
            if word1[i] == word2[j]:
                return dfs(i-1, j-1)

            return min(dfs(i-1,j), dfs(i, j-1), dfs(i-1,j-1)) + 1

        return dfs(len(word1)-1, len(word2)-1)



    def minDistance_2(self, word1:str, word2:str)->int:
        m, n = len(word1), len(word2)
        f = [[0] * (n+1) for _ in range(m+1)]
        f[0] = list(range(n+1))
        for i, x in enumerate(word1):
            f[i+1][0] = i+1
            for j, y in enumerate(word2):
                f[i+1][j+1] = f[i][j] if x == y else \
                    min(f[i+1][j], f[i][j+1], f[i][j])+1

        return f[-1][-1]








