

"""
题目：UTF-8 编码验证

给定一个表示数据的整数数组 data ，返回它是否为有效的 UTF-8 编码。

UTF-8 中的一个字符可能的长度为 1 到 4 字节，遵循以下的规则：

对于 1 字节 的字符，字节的第一位设为 0 ，后面 7 位为这个符号的 unicode 码。
对于 n 字节 的字符 (n > 1)，第一个字节的前 n 位都设为1，第 n+1 位设为 0 ，
后面字节的前两位一律设为 10 。剩下的没有提及的二进制位，全部为这个符号的 unicode 码。
这是 UTF-8 编码的工作方式：

      Number of Bytes  |        UTF-8 octet sequence
                       |              (binary)
   --------------------+---------------------------------------------
            1          | 0xxxxxxx
            2          | 110xxxxx 10xxxxxx
            3          | 1110xxxx 10xxxxxx 10xxxxxx
            4          | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
x 表示二进制形式的一位，可以是 0 或 1。

注意：输入是整数数组。只有每个整数的 最低 8 个有效位 用来存储数据。这意味着每个整数只表示 1 字节的数据。
"""


def validUtf8(data):
    MASK1 = 1 <<7
    MASK2 = (1 << 7) + (1 << 6)

    def getOne(num):
        if num & MASK1 == 0:
            return 1

        mask = MASK1
        n = 0
        while num & mask:
            n+=1
            if n > 4:
                return -1
            mask >>=1
        return n if n >= 2 else -1

    index = 0
    while index < len(data):
        n = getOne(data[index])
        if n < 0 or index+n > len(data) or any((ch & MASK2) != MASK1 for ch in data[index+1: index+n]):
            return False
        index += n
    return True