from collections import Counter


def countPairs(coordinates,k):
    ans = 0
    cnt = Counter()
    for x,y in coordinates:
        for i in range(k+1):
            ans += cnt[x ^ i, y ^ (k - i)]
        cnt[x, y] += 1
    return ans