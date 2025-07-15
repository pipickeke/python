"""
Python中的装饰器是什么？如何实现？

装饰器是修改其他函数功能的函数，使用@语法糖

"""

def my_decorator(func):
    def wrapper():
        print("before func call")
        func()
        print("after func call")
    return wrapper

@my_decorator
def say_hello():
    print("hello")


say_hello()

