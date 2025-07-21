"""
 __new__ 和 __init__ 的区别

"""

class MyClass:
    def __new__(cls, *args, **kwargs):
        print("__new__ is called")
        instance = super().__new__(cls) # 必须调度父类__new__ 并返回实例
        return instance

    def __init__(self, value):
        print("__init__ is called")
        self.value = value

#创建实例
obj = MyClass(10)

print("############# 单例应用场景 ###########")
##### 1，单例应用场景
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("creating new instance")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        print("initializing instance")

#测试
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)


print("######## 2, 限制实例创建 ##########")
class LimitedInstance:
    _count = 0
    _max_instances = 3

    def __new__(cls, *args, **kwargs):
        if cls._count >= cls._max_instances:
            raise RuntimeError(f"cannot create more than {cls._max_instances} instance")
        cls._count += 1
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name

    def __del__(self):
        type(self)._count -= 1

#测试
instances = [LimitedInstance(f"obj{i}") for i in range(3)]
try:
    LimitedInstance("obj4")
except RuntimeError as e:
    print(e)


print("########### 3, 返回不同类型的对象 #########")
class PositiveNumber:
    def __new__(cls, value):
        if value > 0:
            return super().__new__(cls)
        else:
            return None

    def __init__(self, value):
        print(f"initializing positivenumber with value {value}")
        self.value = value


#测试
pos_num = PositiveNumber(10) #正常初始化
print(pos_num.value)

neg_new = PositiveNumber(-10)
print(neg_new)


print("######### 4,元类中使用 __new__ ########")
class Meta(type):
    def __new__(mcls, name, bases, namespace):
        print(f"creating class {name}")
        namespace['version'] = 1.0
        return super().__new__(mcls,name,bases,namespace)









