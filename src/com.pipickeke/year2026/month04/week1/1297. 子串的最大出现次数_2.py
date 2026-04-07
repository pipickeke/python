"""
1297. 子串的最大出现次数

给你一个字符串 s ，请你返回满足以下条件且出现次数最大的 任意 子串的出现次数：

子串中不同字母的数目必须小于等于 maxLetters 。
子串的长度必须大于等于 minSize 且小于等于 maxSize 。


"""
from collections import defaultdict


class Solution:
    def maxFreq(self,s:str, maxLetters:int, minSize:int, maxSize:int)->int:
        str_cnt = defaultdict(int)
        char_cnt = defaultdict(int)

        for i, ch in enumerate(s):
            char_cnt[ch] += 1
            left = i-minSize+1
            if left < 0:
                continue

            if len(char_cnt) <= maxLetters:
                str_cnt[s[left: i+1]] += 1

            out = s[left]
            char_cnt[out] -= 1
            if char_cnt[out] ==0 :
                del char_cnt[out]
        return max(str_cnt.values(), default=0)

