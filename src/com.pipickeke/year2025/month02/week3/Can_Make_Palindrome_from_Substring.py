from typing import List

"""
题目：1177. 构建回文串检测

给你一个字符串 s，请你对 s 的子串进行检测。

每次检测，待检子串都可以表示为 queries[i] = [left, right, k]。我们可以 重新排列 
子串 s[left], ..., s[right]，并从中选择 最多 k 项替换成任何小写英文字母。 

如果在上述检测过程中，子串可以变成回文形式的字符串，那么检测结果为 true，否则结果为 false。

返回答案数组 answer[]，其中 answer[i] 是第 i 个待检子串 queries[i] 的检测结果。

注意：在替换时，子串中的每个字母都必须作为 独立的 项进行计数，也就是说，
如果 s[left..right] = "aaa" 且 k = 2，我们只能替换其中的两个字母。
（另外，任何检测都不会修改原始字符串 s，可以认为每次检测都是独立的）

"""

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        sum = [[0] * 26]
        for c in s:
            sum.append(sum[-1].copy())
            sum[-1][ord(c)-ord('a')] += 1
        ans = []
        for left,right,k in queries:
            m = 0
            for sl,sr in zip(sum[left], sum[right+1]):
                m += (sl - sr) %2
            ans.append(m//2 <= k)
        return ans

    def canMakePaliQueries_2(self, s: str, queries: List[List[int]]) -> List[bool]:
        sum = [[0] * 26]
        for c in s:
            sum.append(sum[-1].copy())
            sum[-1][ord(c) - ord('a')] += 1
            sum[-1][ord(c) - ord('a')] %= 2

        ans = []
        for left,right,k in queries:
            m = 0
            for sl,sr in zip(sum[left], sum[right+1]):
                m += sl != sr
            ans.append(m//2 <= k)
        return ans

    def canMakePaliQueries_3(self, s: str, queries: List[List[int]]) -> List[bool]:
        sum = [[0] * 26]
        for c in s:
            sum.append(sum[-1].copy())
            sum[-1][ord(c)-ord('a')] ^= 1

        ans = []
        for left,right,k in queries:
            m = 0
            for sl,sr in zip(sum[left], sum[right+1]):
                m += sl ^ sr
            ans.append(m//2 <= k)
        return ans

    def canMakePaliQueries_4(self, s: str, queries: List[List[int]]) -> List[bool]:
        sum = [0]
        for c in s:
            bit = 1 << (ord(c)-ord('a'))
            sum.append(sum[-1] ^ bit)
        ans = []
        for left,right,k in queries:
            m = (sum[left] ^ sum[right+1]).bit_count()
            ans.append(m//2 <= k)
        return ans
