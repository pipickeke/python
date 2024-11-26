
"""
题目：消失的两个数字
给定一个数组，包含从 1 到 N 所有的整数，
但其中缺了两个数字。你能在 O(N) 时间内只用 O(1) 的空间找到它们吗？

以任意顺序返回这两个数字均可。

思路：
 *  数组长度为len，消失了2个数，则真正的长度是 len+2
 *  利用异或，计算  1 ~ len+2 的异或和
 *  再去异或数组nums，得到的 x = a ^ b，(a b 就是消失的两个数)
 *  通过计算  lowBit = x & (-x) 得到最右侧的1
 *  然后再去分离剥离出 a b :
 *      (1) lowBit 和 nums数组每个元素求异或和
 *      nums[i] & lowBit == 1 则属于a(  a ^= nums[i] )
 *      nums[i] & lowBit == 0 则属于b(  b ^= nums[i] )
 *      (2) lowBit 和 1 ~ len+2 求异或和
 *      i & lowBit == 1 则属于a(  a ^= i )
 *      i & lowBit == 0 则属于b(  b ^= i )
"""

def miss(arr):
    n = len(arr)
    size = n + 2
    xor = 0
    for i in range(1, size+1):
        xor ^= i

    for j in range(n):
        xor ^= arr[j]

    a = 0
    b = 0
    lowbit = xor & (-xor)
    for p in range(n):
        if arr[p] & lowbit == 0:
            a ^= arr[p]
        else:
            b ^= arr[p]

    for q in range(1, size+1):
        if q & lowbit == 0:
            a = a ^ q
        else:
            b = b ^ q
    return [a,b]

if __name__ == '__main__':
    arr = [1]
    print(miss(arr))