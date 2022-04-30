"""
递归
期望输出：
{
    "a":{
        "b":{
            "c":{
                "d":{}
            }
        }
    }
}
"""


# def f(x, d, idx):
#     if idx == len(d) - 2:
#         return x
#     child = {d[idx+1]: {}}
#     x[d[idx]] = child
#     return f(child, d, idx+1)
# def fun(fat, data, index):
#     if len(data) == index:
#         return {}

#     return {data[index]: fun(fat, data, index+1)}

# data = ('a', 'b', 'c', 'd')
# dd = fun({}, data, 0)
# print(dd)


# data = ("a", "b", "c", "d")
# print(f({}, data, 0))

def fun(data, index):
    if len(data) == index:
        return {}

    return {data[index]: fun(data, index+1)}


# 图中的fat参数用不到
data = ('a', 'b', 'c', 'd', 'e')
dd = fun(data, 0)
print(dd)
