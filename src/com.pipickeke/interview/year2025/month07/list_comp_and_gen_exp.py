
"""
python 中列表推导式和生成器表达式的区别

"""

# 列表推导式
# 会一次性生成所有元素并存储在内存中
lst = [x for x in range(10)] #生成一个列表
print(lst)

# 生成器推导式
# 不会立即生成所有元素，按需逐个生成，通过 next() 迭代
lst_2 = (x for x in range(10)) # 生成一个生成器对象
print(lst_2)


print("##############")
# 列表推导式
nums_list = [x*2 for x in range(10)]
print(f"nums_list: {nums_list}")

# 生成器表达式
nums_gen = (x*2 for x in range(10))
print(next(nums_gen))
print(next(nums_gen))















