



name = 'root'
def outer():
    name = 'abc'
    def inner():
        global name #修改全局变量
        name = 123
    inner()
    print(name)

outer()
print(name)



########################################



tmp = 'root'
def outer():
    tmp = 'abc'
    def inner():
        nonlocal tmp
        tmp = 123
    inner()
    print(tmp) #123, nonlocal 修改上一层，不修改全局

outer()
print(tmp)







