"""
metaclass 测试
"""

#创建自定义元类，需要集成 type 类
# 创建自定义元类
class MyMeta(type):
    def __new__(cls, name, bases, namespace):
        #在类创建之前可以做一些操作
        print(f"Create class {name}")
        return super().__new__(cls, name, bases, namespace)

class MyClass(metaclass=MyMeta):
    pass



