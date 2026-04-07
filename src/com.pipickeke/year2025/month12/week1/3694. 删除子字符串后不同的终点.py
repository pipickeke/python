"""


3694. 删除子字符串后不同的终点


给你一个由字符 'U'、'D'、'L' 和 'R' 组成的字符串 s，表示在无限的二维笛卡尔网格上的移动。

'U': 从 (x, y) 移动到 (x, y + 1)。
'D': 从 (x, y) 移动到 (x, y - 1)。
'L': 从 (x, y) 移动到 (x - 1, y)。
'R': 从 (x, y) 移动到 (x + 1, y)。
你还得到了一个正整数 k。

你 必须 选择并移除 恰好一个 长度为 k 的连续子字符串 s。然后，从坐标 (0, 0) 开始，按顺序执行剩余的移动。

返回可到达的 不同 最终坐标的数量。


"""


class Solution:
    def distinctPoints(self, s:str, k:int) -> int:
        DIRS = {
            'L': (-1,0),
            'R':(1,0),
            'D':(0,-1),
            'U':(0,1)
        }
        st = set()
        x = y = 0
        for i, c in enumerate(s):
            dx, dy = DIRS[c]
            x += dx
            y += dy

            left = i-k+1
            if left<0:
                continue

            st.add((x,y))
            dx,dy = DIRS[s[left]]
            x -= dx
            y -= dy
        return len(st)






    def distinctPoints_2(self, s:str, k:int) -> int:
        DIRS = {
            'U':(0,1),
            'D':(0,-1),
            'L':(-1,0),
            'R':(1,0)
        }
        pos = set()
        x = y = 0
        for i, c in enumerate(s):
            dx,dy = DIRS[c]
            x += dx
            y += dy

            left = i-k+1
            if left < 0:
                continue

            pos.add((x,y))

            dx,dy = DIRS[s[left]]
            x -= dx
            y -= dy
        return len(pos)











