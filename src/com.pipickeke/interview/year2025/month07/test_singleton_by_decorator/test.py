

def testsingle(cls):
    instance = {}
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return  get_instance


@testsingle
class Myclass:
    def __init__(self):
        self.value = "Single"

# 测试
a = Myclass()
b = Myclass()
print(a is b)
