"""



"""
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        s = [0,0]
        max_s1 = 0
        for i, (c, g) in enumerate(zip(customers, grumpy)):
            s[g] += c

            left = i-minutes+1
            if left < 0:
                continue

            max_s1 = max(max_s1, s[1])
            if grumpy[left]:
                s[1] -= customers[left]
        return s[0] + max_s1





    def maxSatisfied_2(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        s = [0,0]
        max_s1 = 0
        for i, (c, g) in enumerate(zip(customers, grumpy)):
            s[g] += c
            left = i-minutes+1
            if left < 0:
                continue
            max_s1 = max(max_s1, s[1])
            if grumpy[left]:
                s[1] -= customers[left]
        return s[0] + max_s1









