
from collections import defaultdict



"""
题目：优美的排列
假设有从 1 到 n 的 n 个整数。
用这些整数构造一个数组 perm（下标从 1 开始），只要满足下述条件 之一 ，
该数组就是一个 优美的排列 ：

perm[i] 能够被 i 整除
i 能够被 perm[i] 整除
给你一个整数 n ，返回可以构造的 优美排列 的 数量 。
"""
def countArrangement(n):
    match = defaultdict(list)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i%j == 0 or j%i ==0:
                match[i].append(j)
    ans = 0
    vis = set()

    def dfs(index):
        if index == n+1:
            nonlocal ans
            ans+=1
            return
        for x in match[index]:
            if x not in vis:
                vis.add(x)
                dfs(index+1)
                vis.discard(x)
    dfs(1)
    return ans


if __name__ == '__main__':
    print(countArrangement(2))
