from typing import List

"""
1691. 堆叠长方体的最大高度
给你 n 个长方体 cuboids ，其中第 i 个长方体的长宽高表示为 cuboids[i] = [widthi, lengthi, heighti]（下标从 0 开始）。请你从 cuboids 选出一个 子集 ，并将它们堆叠起来。

如果 widthi <= widthj 且 lengthi <= lengthj 且 heighti <= heightj ，你就可以将长方体 i 堆叠在长方体 j 上。你可以通过旋转把长方体的长宽高重新排列，以将它放在另一个长方体上。

返回 堆叠长方体 cuboids 可以得到的 最大高度 。

"""

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for c in cuboids:
            c.sort()

        cuboids.sort()
        f = [0] * len(cuboids)
        for x,(_,lx,hx) in enumerate(cuboids):
            for y,(_,ly,hy) in enumerate(cuboids[:x]):
                if ly <= lx and hy <= hx:
                    f[x] = max(f[x], f[y])
            f[x] += hx

        return max(f)