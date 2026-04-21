"""

438. 找到字符串中所有字母异位词

给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，
返回这些子串的起始索引。不考虑答案输出的顺序。


"""
from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s:str, p:str)->List[int]:
        m = len(p)
        if m > len(s):
            return []

        cnt_p = Counter(p)
        cnt_s = Counter()
        ans = []
        for i, ch in enumerate(s):
            cnt_s[ch] += 1
            if i < m-1:
                continue

            if cnt_p == cnt_s:
                ans.append(i-m+1)

            cnt_s[s[i-m+1]] -= 1
        return ans





