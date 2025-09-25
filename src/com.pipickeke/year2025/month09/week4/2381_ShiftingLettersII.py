"""

2381. 字母移位 II

给你一个小写英文字母组成的字符串 s 和一个二维整数数组 shifts ，其中 shifts[i] = [starti, endi, directioni] 。对于每个 i ，将 s 中从下标 starti 到下标 endi （两者都包含）所有字符都进行移位运算，如果 directioni = 1 将字符向后移位，如果 directioni = 0 将字符向前移位。

将一个字符 向后 移位的意思是将这个字符用字母表中 下一个 字母替换（字母表视为环绕的，所以 'z' 变成 'a'）。类似的，将一个字符 向前 移位的意思是将这个字符用字母表中 前一个 字母替换（字母表是环绕的，所以 'a' 变成 'z' ）。

请你返回对 s 进行所有移位操作以后得到的最终字符串。

"""
from itertools import accumulate
from string import ascii_lowercase
from typing import List

c2i = {c: i for i, c in enumerate(ascii_lowercase)}

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff = [0] * (len(s)+1)
        for start,end,val in shifts:
            diff[start] += val*2 - 1
            diff[end+1] -= val*2 -1

        return "".join(ascii_lowercase[(c2i[c]+diff) %26] for c,diff in zip(s, accumulate(diff)))

    def shiftingLetters_2(self, s: str, shifts: List[List[int]]) -> str:
        diff = [0] * (len(s)+1)
        for start,end,val in shifts:
            diff[start] += val*2 -1
            diff[end+1] -= val*2 -1


        return "".join(ascii_lowercase[(c2i[c] + shift) %26] for c,shift in zip(s, accumulate(diff)))







