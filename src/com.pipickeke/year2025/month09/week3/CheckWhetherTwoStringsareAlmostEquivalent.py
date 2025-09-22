"""
2068. 检查两个字符串是否几乎相等

如果两个字符串 word1 和 word2 中从 'a' 到 'z' 每一个字母出现频率之差都 不超过 3 ，那么我们称这两个字符串 word1 和 word2 几乎相等 。

给你两个长度都为 n 的字符串 word1 和 word2 ，如果 word1 和 word2 几乎相等 ，请你返回 true ，否则返回 false 。

一个字母 x 的出现 频率 指的是它在字符串中出现的次数。


"""

class solution:
    def checkAlmostEquivalent(self, word1:str, word2:str)->bool:
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for i in word1:
            cnt1[ord(i)-ord('a')] += 1
        for j in word2:
            cnt2[ord(j)-ord('a')] +=1

        for k, val in enumerate(cnt1):
            if abs(val - cnt2[k]) > 3:
                return False

        return True








