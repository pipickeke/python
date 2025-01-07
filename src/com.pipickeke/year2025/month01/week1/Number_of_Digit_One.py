from functools import cache

"""
题目：233. 数字 1 的个数

给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
"""

def countDigitOne(n):
    s = str(n)

    @cache
    def dfs(i:int, cnt:int, islimit:bool):
        if i == len(s):
            return cnt
        res = 0
        up = int(s[i] if islimit else 9)
        for d in range(up+1):
            res += dfs(i+1, cnt+(d == 1), islimit and d == up)
        return res
    return dfs(0,0,True)