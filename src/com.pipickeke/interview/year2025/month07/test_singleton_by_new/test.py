
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        #初始化只执行一次
        self.value = "Single"

# 测试
a = Singleton()
b = Singleton()

print(a is b)
print(a.value)

