"""

3628. 插入一个字母的最大子序列数

给你一个由大写英文字母组成的字符串 s。

你可以在字符串的 任意 位置（包括字符串的开头或结尾）最多插入一个 大写英文字母。

返回在 最多插入一个字母 后，字符串中可以形成的 "LCT" 子序列的 最大 数量。

子序列 是从另一个字符串中删除某些字符（可以不删除）且不改变剩余字符顺序后得到的一个 非空 字符串。


"""

class Solution:

    def numDistinct(self, s:str, t:str) -> int:
        n = len(t)
        m = len(s)
        dp = [1] + [0] * n

        for i, x in enumerate(s):
            for j in range(min(i, n-1), max(n-m+i,0)-1, -1):
                if x == t[j]:
                    dp[j+1] += dp[j]
        return dp[-1]

    # 计算插入C，额外产生的LCT子序列的个数
    def cal(self, s:str) -> int:
        cnt_t = s.count('T') # s[i+1] ~ s[n-1] 中 T
        cnt_l = 0 # s[0] ~ s[i] 中 L
        res = 0
        for c in s:
            if c == 'T':
                cnt_t -= 1
            if c == 'L':
                cnt_l += 1

            res = max(res, cnt_l * cnt_t)
        return res




    def numOfSubsequences(self, s:str) -> int:
        extra = max(
            self.numDistinct(s, "CT"),
            self.numDistinct(s,"LC"),
            self.cal(s)
        )
        return self.numDistinct(s,"LCT") + extra



