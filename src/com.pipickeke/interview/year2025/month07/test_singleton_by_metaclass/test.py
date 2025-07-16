
class SingletonMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = "single"

# 测试
a = Singleton()
b = Singleton()
print(a is b)



