"""
Python 的 GIL（全局解释器锁）
:
GIL 是python解释器中的一个机制，
确保同一时刻只有一个线程可以执行python代码，
意味着即使在多核cpu中，python的多线程程序也无法
实现的真正的并行执行

"""

# 1， CPU 密集型任务，受 GIL 限制
import threading
import time

def count_down(n):
    while n > 0:
        n -=1

#单线程执行
start = time.time()
count_down(100000000)
count_down(100000000)
end = time.time()
print(f"执行时间：{end - start:.2f}秒")

# 多线程执行
start = time.time()
t1 = threading.Thread(target=count_down, args=(100000000,))
t2 = threading.Thread(target=count_down, args=(100000000,))
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(f"多线程执行时间: {end - start:.2f}秒")

"""
执行时间：8.62秒
多线程执行时间: 8.73秒
"""

# 2, I/O 密集任务，GIL影响小
import requests

# def download_url(url):