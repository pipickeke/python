from typing import List

"""
题目：2935. 找出强数对的最大异或值 II
标签：字典树

给你一个下标从 0 开始的整数数组 nums 。如果一对整数 x 和 y 满足以下条件，则称其为 强数对 ：

|x - y| <= min(x, y)
你需要从 nums 中选出两个整数，且满足：这两个整数可以形成一个强数对，
并且它们的按位异或（XOR）值是在该数组所有强数对中的 最大值 。

返回数组 nums 所有可能的强数对中的 最大 异或值。

注意，你可以选择同一个整数两次来形成一个强数对。


"""


class Node:

    __slots__ = 'children', 'cnt'

    def __init__(self):
        self.children = [None, None]
        self.cnt = 0

class Trie:
    HIGH_BIT = 19
    def __init__(self):
        self.root = Node()

    def insert(self, val: int):
        cur = self.root
        for i in range(Trie.HIGH_BIT,-1,-1):
            bit = (val >> i) & 1
            if cur.children[bit]  is None:
                cur.children[bit] = Node()
            cur = cur.children[bit]
            cur.cnt += 1
        return cur

    def remove(self, val: int):
        cur = self.root
        for i in range(Trie.HIGH_BIT,-1,-1):
            cur = cur.children[(val >> i) &1]
            cur.cnt -= 1
        return cur

    def maxxor(self, val: int):
        cur = self.root
        ans = 0
        for i in range(Trie.HIGH_BIT,-1,-1):
            bit = (val >>i) &1
            if cur.children[bit ^ 1] and cur.children[bit ^ 1].cnt:
                ans |= (1 <<i)
                bit ^= 1
            cur = cur.children[bit]
        return ans


class Solution:
    def maximumStrongPairXor(self, nums: List[int]):
        nums.sort()
        t = Trie()
        ans = left = 0
        for y in nums:
            t.insert(y)
            while nums[left] * 2 < y:
                t.remove(nums[left])
                left += 1
            ans = max(ans, t.maxxor(y))
        return ans


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    s = Solution();
    print(s.maximumStrongPairXor(nums))












