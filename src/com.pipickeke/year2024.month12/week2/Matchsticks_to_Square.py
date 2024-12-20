


"""
题目：火柴拼正方形

你将得到一个整数数组 matchsticks ，其中 matchsticks[i] 是第 i 个火柴棒的长度。
你要用 所有的火柴棍 拼成一个正方形。你 不能折断 任何一根火柴棒，
但你可以把它们连在一起，而且每根火柴棒必须 使用一次 。

如果你能使这个正方形，则返回 true ，否则返回 false 。

"""

def makesquare(matchsticks):
    sumTotal = sum(matchsticks)
    if sumTotal % 4 :
        return False
    matchsticks.sort(reverse=True)

    edges = [0] *4
    def dfs(idx):
        if idx == len(matchsticks):
            return True
        for i in range(4):
            edges[i] += matchsticks[idx]
            if edges[i] <= sumTotal //4 and dfs(idx+1):
                return True
        return False
    dfs(0)





