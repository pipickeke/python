"""
30. 串联所有单词的子串

给定一个字符串 s 和一个字符串数组 words。 words 中所有字符串 长度相同。

 s 中的 串联子串 是指一个包含  words 中所有字符串以任意顺序排列连接起来的子串。

例如，如果 words = ["ab","cd","ef"]， 那么 "abcdef"， "abefcd"，"cdabef"， "cdefab"，"efabcd"， 和 "efcdab" 都是串联子串。 "acdbef" 不是串联子串，因为他不是任何 words 排列的连接。
返回所有串联子串在 s 中的开始索引。你可以以 任意顺序 返回答案。
"""
from collections import Counter, defaultdict
from typing import List


class Solution:
    def findSubstring(self, s:str, words:List[str])->List[int]:
        word_len = len(words[0])
        window_len = word_len * len(words)
        target = Counter(words)

        ans = []
        for start in range(word_len):
            cnt = defaultdict(int)
            overload = 0
            for right in range(start+word_len, len(s)+1, word_len):
                in_word = s[right-word_len:right]
                if cnt[in_word] == target[in_word]:
                    overload += 1
                cnt[in_word] += 1

                left = right-window_len
                if left < 0:
                    continue

                if overload == 0:
                    ans.append(left)

                out_word = s[left:left+word_len]
                cnt[out_word] -= 1
                if cnt[out_word] == target[out_word]:
                    overload -= 1

        return ans

