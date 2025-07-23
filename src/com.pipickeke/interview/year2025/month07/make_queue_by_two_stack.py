
"""

用两个栈实现一个队列

"""

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x:int) ->None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


if __name__ == '__main__':
    myQueue = MyQueue()
    #测试空队列
    print(f"空队列：{myQueue.empty()}")

    #测试push peek
    myQueue.push(1)
    print(f"peek: {myQueue.peek()}")
    print(f"是否为空: {myQueue.empty()}")