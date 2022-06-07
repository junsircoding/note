#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : Scripts/25-多轮对话字典数据处理.py
# @Info        : 
# @Last Edited : 2022-06-07 11:19:15

"""
字典数据处理
"""
import pprint as pp

data_0 = [
    ("高血压", "一级问", "是", "是_二级问", "是", "拒保",),
    ("高血压", "一级问", "是", "是_二级问", "否", "投保",),
    ("高血压", "一级问", "否", "否_二级问", "是", "拒保2",),
    ("高血压", "一级问", "否", "否_二级问", "否", "答案2",),
    ("高血压", "一级问2", "空值", "空值", "空值", "推保险",),
]
print("---data_0")
pp.pprint(data_0)

"""
1.去除每一行的`空值`
"""
data_1 = []
for item in data_0:
    data_1.append(tuple(filter(lambda i: i != "空值", item)))
print("---data_1")
pp.pprint(data_1)
# [('高血压', '拒保'), ('高血压', '一级问', '是', '二级问', '是', '拒保')]

"""
2.递归访问每一行数据，返回字典串
"""


def demo(dataset, idx):
    if len(dataset) == idx+1:
        return dataset[idx]
    return {
        dataset[idx]: demo(dataset, idx+1)
    }


data_2 = []
for item in data_1:
    data_2.append(demo(item, 0))
print("---data_2")
pp.pprint(data_2)

"""
3.合并所有数据，不覆盖相同键
```python
{
    "高血压": {
        "一级问": {
            "是": {
                "是_二级问": {
                    "是": "拒保",
                    "否": "投保"
                }
            },
            "否": {
                "否_二级问": {
                    "是": "拒保2",
                    "否": "答案2"
                }
            }
        },
        "一级问2":"推保险"
    }
}
```
"""

result = {}
for first in data_2:
    first_key = list(first.keys())[0]
    if first_key in result:
        second = first[first_key]
        second_key_list = list(second.keys())
        for second_key in second_key_list:
            if second_key in result[first_key]:
                third = second[second_key]
                third_key_list = list(third.keys())
                for third_key in third_key_list:
                    if third_key in result[first_key][second_key]:
                        forth = third[third_key]
                        forth_key_list = list(forth.keys())
                        for forth_key in forth_key_list:
                            if forth_key in result[first_key][second_key][third_key]:
                                fifth = forth[forth_key]
                                fifth_key_list = list(fifth.keys())
                                for fifth_key in fifth_key_list:
                                    if fifth_key in result[first_key][second_key][third_key][forth_key]:
                                        sixth = fifth[fifth_key]
                                    else:
                                        result[first_key][second_key][third_key][forth_key][fifth_key] = fifth[fifth_key]
                            else:
                                result[first_key][second_key][third_key][forth_key] = forth[forth_key]
                    else:
                        result[first_key][second_key][third_key] = third[third_key]
            else:
                result[first_key][second_key] = second[second_key]
    else:
        result[first_key] = first[first_key]
print("---result")
pp.pprint(result)
