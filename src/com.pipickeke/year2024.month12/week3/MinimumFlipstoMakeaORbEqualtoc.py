

"""
题目：1318. 或运算的最小翻转次数

给你三个正整数 a、b 和 c。

你可以对 a 和 b 的二进制表示进行位翻转操作，返回能够使按位或运算
  a OR b == c  成立的最小翻转次数。

「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0 或者 0 变成 1 。

"""

def minFlips(a,b,c):
    ans = 0
    for i in range(32):
        bita = (a >>i) &1
        bitb = (b >>i) &1
        bitc = (c >>i) &1
        if bitc == 0:
            ans += bita + bitb
        else:
            ans += int(bita + bitb == 0)
    return ans