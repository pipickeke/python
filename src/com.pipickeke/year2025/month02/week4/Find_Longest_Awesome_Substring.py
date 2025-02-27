"""
题目：1542. 找出最长的超赞子字符串

给你一个字符串 s 。请返回 s 中最长的 超赞子字符串 的长度。

「超赞子字符串」需满足满足下述两个条件：

该字符串是 s 的一个非空子字符串
进行任意次数的字符交换后，该字符串可以变成一个回文字符串


"""

class Solution:
    def longestAwesome(self, s: str) -> int:
        NUMS = 10
        n = len(s)
        pos = [n] * (1 << NUMS)
        pos[0] = -1

        pre = ans = 0
        for i,x in enumerate(map(int, s)):
            pre ^= 1 << x
            ans = max(ans, i - pos[pre],
                      max(i - pos[pre ^ (1 << d)] for d in range(NUMS)))

            if pos[pre] == n:
                pos[pre] = i
        return ans

