

"""
题目：汉明距离总和
两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。

给你一个整数数组 nums，请你计算并返回 nums 中任意两个数之间 汉明距离的总和 。
"""

def totalHammingDistance(nums):
    n = len(nums)
    ans = 0
    for i in range(30):
        c = sum(( (val >>i) &1) for val in nums)
        ans += c * (n-c)
    return ans

if __name__ == '__main__':
    arr = [4,14,2]
    print(totalHammingDistance(arr))

