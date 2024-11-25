


"""
题目：冒泡排序
"""
def bubble1(arr):
    N = len(arr)
    for i in range(N):
        for j in range(N-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


"""
优化版本
"""
def bubble2(arr):
    N = len(arr)
    for i in range(N):
        swap = False
        for j in range(N-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            break
    return arr




if __name__ == '__main__':
    arr = [6,2,8,1,0,4]
    bubble2(arr)
    print(arr)