
from collections import defaultdict


"""
题目：重复的DNA序列
DNA序列 由一系列核苷酸组成，缩写为 'A', 'C', 'G' 和 'T'.。

例如，"ACGAATTCCG" 是一个 DNA序列 。
在研究 DNA 时，识别 DNA 中的重复序列非常有用。

给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的 
长度为 10 的序列(子字符串)。你可以按 任意顺序 返回答案。

思路：哈希表
"""
def findRepeatedDnaSequences(s):
    ans = []
    L = 10
    cnt = defaultdict(int)
    for i in range(len(s)-L+1):
        sub = s[i:i+L]
        cnt[sub] += 1
        if cnt[sub] == 2:
            ans.append(sub)
    return ans


bin = {'A':0, 'C':1, 'G':2, 'T':3}
L = 10
def findRepeatedDnaSequences(s):
    n = len(s)
    if n <= L:
        return []

    x = 0
    for i in range(L-1):
        x = x



def zero():
    return 0

if __name__ == '__main__':
    # print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

    """
    defaultdict 函数使用
    """
    dd = defaultdict(list)
    print('aa' in dd)
    print(dd.get('aa'))
    print(dd['aa'])

    aa = defaultdict(zero)
    print(aa['aa'])
    print(aa.get('aa'))

    strings = ('puppy','puppy','kitten')
    # counts = defaultdict(lambda:0)
    counts = defaultdict(int)
    for s in strings:
        counts[s] += 1
    print(counts)








