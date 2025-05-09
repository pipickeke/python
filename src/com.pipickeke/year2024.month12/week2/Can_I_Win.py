from functools import cache


"""
题目：我能赢吗

在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，
累计整数和，先使得累计整数和 达到或超过  100 的玩家，即为胜者。

如果我们将游戏规则改为 “玩家 不能 重复使用整数” 呢？

例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），
直到累计整数和 >= 100。

给定两个整数 maxChoosableInteger （整数池中可选择的最大数）和 desiredTotal（累计和），
若先出手的玩家能稳赢则返回 true ，否则返回 false 。假设两位玩家游戏时都表现 最佳 。

 
"""

def canIWin(maxChoosableInteger, desiredTotal):

    @cache
    def dfs(record, sum):
        for i in range(1, maxChoosableInteger+1):
            if (record >>i) & 1 ==0:
                if sum+i >= desiredTotal or not dfs( record | (1 <<i), sum+i ):
                    return True
        return False

    return (1+maxChoosableInteger)*maxChoosableInteger // 2 >= desiredTotal and dfs(0,0)



