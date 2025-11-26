"""



"""


class Solution:
    def numOfSubsequences(self, s:str)->int:
        extra = max(
            self.f1(s, "CT"),
            self.f1(s, "LC"),
            self.f2(s)
        )
        return self.f1(s, "LCT") + extra


    def f1(self, s:str, t:str):
        m,n = len(s), len(t)
        dp = [1] + [0] * n

        for i, x in enumerate(s):
            for j in range(min(n-1, i), max(n-m+i, 0)-1, -1):
                if x == t[j]:
                    dp[j+1] += dp[j]
        return dp[-1]

    def f2(self, s:str)->int:
        cnt_t = s.count('T')
        cnt_l = 0
        res = 0
        for c in s:
            if c == 'T':
                cnt_t -= 1
            if c == 'L':
                cnt_l += 1
            res = max(res, cnt_l * cnt_t)
        return res







