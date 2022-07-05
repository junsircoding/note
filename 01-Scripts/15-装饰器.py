"""
不要使用可变对象作为参数默认值
"""
def foo(x, items=[]):
    items.append(x)
    print(items)

foo(1)
foo(2)
foo(3)

"""
输出:
[1]
[1, 2]
[1, 2, 3]
"""

def foo_1(x, items=None):
    if items is None:
        items = []
    items.append(x)
    print(items)

foo_1(1)
foo_1(2)
foo_1(3)

"""
[1]
[2]
[3]
"""

"""
*args 可以接受任意数量的参数
"""
def fprintf(file, fmt, *args):
    file.write(fmt % args)

with open("test.txt", "w", encoding="utf-8") as out:
    fprintf(out, "%d %s %f", 42, "hello world", 3.45)
"""
test.txt
42 hello world 3.450000
"""

import sys

def printf(fmt, *args):
    fprintf(sys.stdout, fmt, *args)

printf("%d %s %f", 42, "hello world", 3.45)
"""
42 hello world 3.450000% 
"""
print()

def foo_2(x, y, z, w):
    print("%s-%s-%s-%s" % (x, y, z, w))

# foo("hello", 3, z=[1,2], y=22) # TypeError: foo() got multiple values for argument 'y'
foo_2(x=3, y=22, w="hello", z=[1,2])
foo_2(3, 33, w="hello", z=[1,2])

"""
**kwargs 接受余下所有的参数, 带参数名称
"""
def make_table(data, **params):
    # 从 params (字典)获取配置参数
    fgcolor = params.pop("fgcolor", "black")
    bgcolor = params.pop("bgcolor", "white")
    width = params.pop("width", None)
    if params:
        raise TypeError("不支持的配置项 %s" % list(params))

items = [1,2,3,4,5]
# make_table(
#     items, fgcolor="black", bgcolor="white", border=1,
#     borderstyle="grooved", cellpadding=10, width=400
# )
"""
TypeError: 不支持的配置项 ['border', 'borderstyle', 'cellpadding']
"""

"""接受数量不定的位置关键字参数"""
def spam(*args, **kwargs):
    """这个函数接受参数的任意组合
    *args 和 **kwargs 通常用来为其他函数编写包装器和代理

    args: 位置参数的元祖
    kwargs: 关键字参数的字典
    """

"""
如果传递不可变的值, 参数是按值传递
如果传递可变对象(如列表或字典), 然后再修改此可变对象, 这些改动将反映在原始对象中, 这就是引用传递
"""
a = [1, 2, 3, 4, 5, 6]
print(a)
def square(items):
    for i, x in enumerate(items):
        items[i] = x*x # 原地修改 items 中的元素
square(a)
print(a)
"""
[1, 2, 3, 4, 5, 6]
[1, 4, 9, 16, 25, 36]
这样的程序有副作用, 不要这样编程, 出现 bug 根本找不出来
"""

"""
命名空间中的一个特别之处是在函数中对全局变量的操作
"""
a = 42
print(a)
def foo_3():
    a = 13
foo_3()
print(a)
# a 仍然是 42

b = 56
print(b)
def foo_4():
    global b
    b = 3
foo_4()
print(b)
# 修改成功

def countdown(start):
    n = start
    def display():
        print("T-minus %d" % n)
    def decrement():
        nonlocal n # 绑定外部的 n, 仅限 Python3 使用
        n -= 1
    while n > 0:
        display()
        decrement()

"""作为对象与闭包的函数"""
def callf(func):
    return func()
"""把函数当作数据处理时, 它将隐式地携带与定义该函数的周围环境相关的信息
这将影响到函数中自由变量的绑定方式"""

x = 42
def callf_2(func):
    return func()



