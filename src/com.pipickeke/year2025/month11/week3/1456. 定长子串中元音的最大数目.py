"""




"""

class Solution:
    def maxVowels(self, s:str,k:int)->int:
        ans = tmp = 0
        for i, x in enumerate(s):
            if x in 'aeiou':
                tmp += 1

            left = i-k+1
            if left < 0:
                continue

            ans = max(ans, tmp)

            if s[left] in 'aeiou':
                tmp -= 1

        return ans



    def maxVowels_2(self, s:str,k:int)->int:
        ans = tmp = 0
        for i, x in enumerate(s):
            if x in 'aeiou':
                tmp += 1

            left = i-k+1
            if left < 0:
                continue

            ans = max(ans, tmp)
            if s[left] in 'aeiou':
                tmp -= 1

        return ans






