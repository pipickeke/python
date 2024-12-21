from collections import Counter
from itertools import accumulate
from operator import xor


def beautifulSubarrays(nums):
    s = list(accumulate(nums, xor, initial=0))
    ans, cnt = 0, Counter()
    for x in s:
        ans += cnt[x]
        cnt[x] += 1
    return ans



