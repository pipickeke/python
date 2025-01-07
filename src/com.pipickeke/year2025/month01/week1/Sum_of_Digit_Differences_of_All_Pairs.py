
"""
题目：3153. 所有数对中数位差之和

你有一个数组 nums ，它只包含 正 整数，所有正整数的数位长度都 相同 。

两个整数的 数位差 指的是两个整数 相同 位置上不同数字的数目。

请你返回 nums 中 所有 整数对里，数位差之和。


"""


def sumDigitDifferences(nums):
    ans = 0
    matrix = [[0] *10 for _ in str(nums[0])]
    for k, x in enumerate(nums):
        i = 0
        while x:
            x, d = divmod(x,10)
            ans += k - matrix[i][d]
            matrix[i][d] += 1
            i += 1
    return ans

