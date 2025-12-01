"""

2379. 得到 K 个黑块的最少涂色次数

给你一个长度为 n 下标从 0 开始的字符串 blocks ，blocks[i] 要么是 'W' 要么是 'B' ，表示第 i 块的颜色。字符 'W' 和 'B' 分别表示白色和黑色。

给你一个整数 k ，表示想要 连续 黑色块的数目。

每一次操作中，你可以选择一个白色块将它 涂成 黑色块。

请你返回至少出现 一次 连续 k 个黑色块的 最少 操作次数。


"""
from math import inf


class Solution:
    def minimumRecolors(self, blocks:str, k:int) -> int:
        s = 0
        ans = inf
        for i, x in enumerate(blocks):
            if x == 'W':
                s += 1
            left = i-k+1
            if left < 0:
                continue

            ans = min(ans, s)
            s -= (1 if blocks[left] == 'W' else 0)
        return ans



    def minimumRecolors_2(self, blocks:str, k:int) -> int:
        s = 0
        ans = inf
        for i, x in enumerate(blocks):
            if x == 'W':
                s += 1
            left = i-k+1
            if left < 0:
                continue
            ans = min(ans, s)
            s -= (1 if blocks[left] == 'W' else 0)
        return ans
