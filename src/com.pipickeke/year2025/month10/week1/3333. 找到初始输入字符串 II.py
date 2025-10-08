"""




"""
from itertools import accumulate


class Solution:
    def possibleStringCount(self, word:str, k:int)->int:
        n = len(word)
        if n < k:
            return 0

        MOD = int(1e9 + 7)
        cnts = []
        cnt = 0
        ans = 1
        for i in range(n):
            cnt += 1
            if i == n-1 or word[i] != word[i+1]:
                if cnt > 1:
                    if k > 0:
                        cnts.append(cnt-1)
                    ans = ans * cnt % MOD
                k -= 1
                cnt = 0

        if k <= 0:
            return ans

        f = [[0] * k for _ in range(len(cnts)+1)]
        f[0] = [1] * k
        for i, c in enumerate(cnts):
            s = list(accumulate(f[i], initial=0))
            for j in range(k):
                f[i+1][j] = (s[j+1] - s[max(j-c, 0)]) % MOD

        return (ans - f[-1][-1]) % MOD







    def possibleStringCount_2(self, word:str, k:int)->int:
        n = len(word)
        if n < k:
            return 0

        cnts = []
        cnt = 0
        ans = 1
        MOD = int(1e9 + 7)
        for i in range(n):
            cnt += 1
            if i == n-1 or word[i] != word[i+1]:
                if cnt > 1:
                    if k > 0:
                        cnts.append(cnt-1)
                    ans = ans * cnt % MOD

                k -= 1
                cnt = 0

        if k <= 0:
            return ans

        f = [[0] * k for _ in range(len(cnts)+1)]
        f[0] = [1] * k
        for i, c in enumerate(cnts):
            s = list(accumulate(f[i], initial=0))
            for j in range(k):
                f[i+1][j] = (s[j+1] - s[max(j-c, 0)]) % MOD


        return (ans - f[-1][-1]) % MOD







    def possibleStringCount_3(self, word:str, k:int)->int:
        n = len(word)
        if n < k:
            return 0

        cnt = 0
        cnts = []
        ans = 1
        MOD = int(1e9 + 7)
        for i in range(n):
            cnt += 1
            if i == n-1 or word[i] != word[i+1]:
                if cnt > 1:
                    if k > 0:
                        cnts.append(cnt-1)
                    ans = ans * cnt % MOD

                k -= 1
                cnt = 0

        if k <= 0:
            return ans

        f = [[0] * k for _ in range(len(cnts)+1)]
        f[0] = [1]*k
        for i, c in enumerate(cnts):
            s = list(accumulate(f[i], initial=0))
            for j in range(k):
                f[i+1][j] = (s[j+1] - s[max(j-c, 0)]) % MOD

        return (ans - f[-1][-1]) % MOD






    def possibleStringCount_4(self, word:str, k:int)->int:
        n = len(word)
        if n < k:
            return 0

        cnts = []
        cnt = 0
        ans = 1
        MOD = int(1e9 + 7)
        for i in range(n):
            cnt += 1
            if i == n-1 or word[i] != word[i+1]:
                if cnt > 1:
                    if k > 0:
                        cnts.append(cnt-1)

                k -= 1
                cnt = 0




