"""

567. 字符串的排列

给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的 排列。如果是，返回 true ；否则，返回 false 。

换句话说，s1 的排列之一是 s2 的 子串 。

"""
from collections import Counter


class Solution:
    def checkInclusion(self, s1:str, s2:str)->bool:
        m = len(s1)
        if m > len(s2):
            return False

        s1_cnt = Counter(s1)
        s2_cnt = Counter()
        for i, ch in enumerate(s2):
            s2_cnt[ch] += 1
            if i < m-1:
                continue

            if s2_cnt == s1_cnt:
                return True

            s2_cnt[s2[i-m+1]] -= 1
        return False

