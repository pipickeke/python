"""
Python如何实现单例模式？其他23种设计模式python如何实现

"""

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


########## 1, 通过模块实现单例模式
from utils.MySingleton import instance
instance.value = "hello"
print(instance.value)


######### 2, 使用装饰器实现单例模式
def singleton_2(cls):
    instance = {}
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return get_instance

@singleton_2
class MyClass:
    def __init__(self):
        self.value = "Singleton"

#测试
a = MyClass()
b = MyClass()
print(a is b)





