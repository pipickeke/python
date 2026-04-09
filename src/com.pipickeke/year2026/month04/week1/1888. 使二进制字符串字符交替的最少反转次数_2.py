"""

1888. 使二进制字符串字符交替的最少反转次数

给你一个二进制字符串 s 。你可以按任意顺序执行以下两种操作任意次：

类型 1 ：删除 字符串 s 的第一个字符并将它 添加 到字符串结尾。
类型 2 ：选择 字符串 s 中任意一个字符并将该字符 反转 ，也就是如果值为 '0' ，则反转得到 '1' ，反之亦然。
请你返回使 s 变成 交替 字符串的前提下， 类型 2 的 最少 操作次数 。

我们称一个字符串是 交替 的，需要满足任意相邻字符都不同。

比方说，字符串 "010" 和 "1010" 都是交替的，但是字符串 "0100" 不是。

"""
class Solution:
    def minFlips(self, s:str)->int:
        n = len(s)
        target = "01"
        cnt = 0

        for i in range(n):
            cnt += 1 if s[i] != target[i%2] else 0

        ans = min(cnt, n-cnt)

        for i in range(n):
            cnt -= 1 if s[i] != target[i % 2] else 0
            cnt += 1 if s[i] != target[(i+n) % 2] else 0
            ans = min(ans, cnt, n-cnt)
        return ans






