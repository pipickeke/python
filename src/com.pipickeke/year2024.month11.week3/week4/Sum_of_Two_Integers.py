

"""
题目：两整数之和
给你两个整数 a 和 b ，
不使用 运算符 + 和 -，计算并返回两整数之和。

思路：
python中整数类型是无限长，所以无论左移多少位都不会溢出。
需要利用掩码 2^32， 将整数对  2^32 取模，从而使得第33及更高位都是0,

"""
def getSum(a, b):
    mask1 = pow(2,32)
    mask2 = pow(2,31)
    mask3 = pow(2,31)-1
    a = a % mask1
    b = b % mask1
    while b != 0:
        carry = ((a & b) <<1) % mask1
        a = (a^b) % mask1
        b = carry
    if a & mask2: #负数
        return ~((a ^ mask2) ^ mask3)
    else:
        return a

if __name__ == '__main__':
    a = 1
    b = 2
    print(getSum(a, b))
