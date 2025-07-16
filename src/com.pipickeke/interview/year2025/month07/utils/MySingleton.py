

"""

通过模块，实现单例

在python中，模块本身就是单例，python只会加载一次模块，
可以利用模块实现单例
"""

class MySingleton:
    def __init__(self):
        self.value = None

instance = MySingleton()