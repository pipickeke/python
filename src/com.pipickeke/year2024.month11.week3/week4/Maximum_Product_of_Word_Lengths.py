from functools import reduce
from itertools import product

"""
题目：最大单词长度乘积
给你一个字符串数组 words ，找出并返回 length(words[i]) * length(words[j]) 的最大值，
并且这两个单词不含有公共字母。如果不存在这样的两个单词，返回 0 。

函数介绍：
（1） reduce() 对参数序列中元素进行累积
    reduce(function, iterable[, initializer])
            函数，迭代参数，初始值
    
"""


def maxProduct(words):
    masks = [reduce(lambda a, b: a | (1 << (ord(b) - ord('a'))), word, 0) for word in words]
    return max((len(x[1]) * len(y[1]) for x, y in product(zip(masks, words), repeat=2) if x[0] & y[0] == 0), default=0)


def add(x, y):
    return x + y


if __name__ == '__main__':
    # print(maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))

    sum1 = reduce(add, [1, 2, 3, 4])
    print(sum1)
    sum2 = reduce(lambda a, b: a + b, [1, 2, 3])
    print(sum2)


    sum3 = reduce(lambda a, b: a + b, [1, 2, 3], 10)
    print(sum3)