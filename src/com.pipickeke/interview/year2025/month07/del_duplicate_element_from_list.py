"""
请写出一段Python代码实现删除一个list里面的重复元素
"""

l = [1,1,1,2,3,4]

# 方法1
print(list(set(l)))
#print(set(l))


d = {}
for x in l:
    d[x] = 1
print(d)
print(d.keys())
print(list(d.keys()))


