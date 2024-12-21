

"""

python3.9 引入的 @cache 缓存装饰器，在 functools 模块中
通过缓存函数的输入和返回结果，当函数被再次调用时，
如果输入参数相同，则直接从缓存返回结果，避免了重复计算或io操作

引入  @cache，可以加速 60%

"""
import random
import time
from functools import cache

sample_num = 10000
repeat_num = 10
target_order = ['Y','C','J','D','S','G']
order = {char: i for i, char in enumerate(target_order)}
whole_sample = []

for i in range(sample_num):
    num_to_select = random.randint(1, len(target_order))
    selected_values = random.sample(target_order, num_to_select)
    random.shuffle(selected_values)
    whole_sample.append(selected_values)

@cache
def sort1(cur_sample):
    return sorted(cur_sample, key=order.get())

def test():
    start1 = time.perf_counter()
    for i in range(repeat_num):
        sorted_samples = []
        for sample in whole_sample:
            sorted_samples.append(sorted(sample, key=order.get()))
    speed = (time.perf_counter() - start1) / repeat_num
    print("直接排序用时：{}".format(speed))

    start2 = time.perf_counter()
    for i in range(repeat_num):
        sorted_samples = []
        for sample in whole_sample:
            sorted_samples.append(sort1(tuple(sample)))
        speed = ()












