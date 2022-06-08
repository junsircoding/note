#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding@gmail.com
# @File        : 11-协程/asyncio_prac.py
# @Info        : 
# @Last Edited : 2022-06-08 18:04:57

# import asyncio

# async def count():
#     print("One")
#     await asyncio.sleep(1)
#     print("Two")

# async def main():
#     await asyncio.gather(count(), count(), count())

# if __name__ == "__main__":
#     import time
#     s = time.perf_counter()
#     asyncio.run(main())
#     elapsed = time.perf_counter() - s
#     print(f"{__file__} executed in {elapsed:0.2f} seconds.")

# import time

# def count():
#     print("One")
#     time.sleep(1)
#     print("Two")

# def main():
#     for _ in range(3):
#         count()

# if __name__ == "__main__":
#     s = time.perf_counter()
#     main()
#     elapsed = time.perf_counter() - s
#     print(f"{__file__} executed in {elapsed:0.2f} seconds.")

# rand.py

# import asyncio
# import random

# # ANSI colors
# routine_data = {
#     "0_CYAN": {
#         "color":"\033[36m",
#         "cost": 2,
#         "threshold": 6,
#         "name": "青色协程"
#     },  # 青色, Cyan
#     "1_RED": {
#         "color": "\033[91m",
#         "cost": 3,
#         "threshold": 7,
#         "name": "鲜红协程"
#     },  # 鲜红, Red
#     "2_Magenta": {
#         "color": "\033[35m",
#         "cost": 4,
#         "threshold": 8,
#         "name": "品红协程"
#     },  # 品红, Magenta
#     "3_END": {
#         "color": "\033[0m",
#         "cost": 5,
#         "threshold": 9,
#         "name": "结束协程"
#     }   # 结束颜色
# }

# async def makerandom(color: str) -> int:
#     """生成随机数

#     Args:
#         idx(str): 颜色索引
#         threshold(int): 阈值
#     Returns:
#         (int): 随机数
#     """
#     routine_name = routine_data[color]["name"]
#     routine_color = routine_data[color]["color"]
#     routine_cost = routine_data[color]["cost"]
#     routine_threshold = routine_data[color]["threshold"]

#     print(routine_color + f"[{routine_name}]的目标阈值为, 需耗时 {routine_cost} 秒")

#     new_random_num = random.randint(0, 10)
#     while new_random_num <= routine_threshold:
#         print(routine_color + f"[{routine_name}]生成的随机数为: {new_random_num}, 小于阈值 {routine_threshold}, 重试...")
#         await asyncio.sleep(routine_cost)
#         new_random_num = random.randint(0, 10)
#     print(routine_color + f"[{routine_name}]生成的随机数为: {new_random_num}, 完成." + routine_data["3_END"]["color"])
#     return new_random_num

# async def main():
#     """开启三个生成随机数协程"""
#     res = await asyncio.gather(
#         *[
#             makerandom("0_CYAN"),
#             makerandom("1_RED"),
#             makerandom("2_Magenta")
#         ]
#     )
#     return res

# if __name__ == "__main__":
#     # 设定随机数生成器的种子, 预先设置种子, 第一次生成的随机数会是同一个
#     random.seed(444)
#     # 执行协程
#     r1, r2, r3 = asyncio.run(main())
#     print()
#     # 打印结果
#     print(f"r1: {r1}, r2: {r2}, r3: {r3}")

# import asyncio
# import random
# import time

# from matplotlib.pyplot import step

# async def part1(step_idx: int) -> str:
#     """函数一
#     Args:
#         step_idx(int): 步骤序号
#     Returns:
#         (str): 步骤结果
#     """
#     cost_time = random.randint(0, 10)
#     print(f"函数一的第[{step_idx}]步, 耗时 {cost_time} 秒.")
#     await asyncio.sleep(cost_time)
#     result = f"[1.{step_idx}]"
#     print(f"函数一的第[{step_idx}]步结果为: {result}.")
#     return result

# async def part2(step_idx: int, arg: str) -> str:
#     """函数二
#     Args:
#         step_idx(int): 步骤序号
#     Returns:
#         (str): 步骤结果
#     """
#     cost_time = random.randint(0, 10)
#     print(f"函数二的第[{step_idx}]步, 参数: {arg} 耗时 {cost_time} 秒.")
#     await asyncio.sleep(cost_time)
#     result = f"[2.{step_idx}]({arg})"
#     print(f"函数二的第[{step_idx}]步结果为: {result}.")
#     return result

# async def chain(step_idx: int) -> None:
#     """链接器, 分别将两个函数的每个步骤结果链接起来
#     Args:
#         step_idx(int): 步骤序号
#     """
#     start = time.perf_counter()
#     p1 = await part1(step_idx)
#     p2 = await part2(step_idx, p1)
#     end = time.perf_counter() - start
#     print(f"-->步骤[{step_idx}]链接完成, 结果为: {p2}, 花费 {end:0.2f} 秒.")

# async def main(*args):
#     """批量执行协程"""
#     await asyncio.gather(*(chain(n) for n in args))

# if __name__ == "__main__":
#     # 设置出事随机数种子
#     random.seed(444)
#     # 设置步骤序号
#     args = [1, 2, 3]
#     start = time.perf_counter()
#     asyncio.run(main(*args))
#     end = time.perf_counter() - start
#     print(f"程序耗时 {end:0.2f} 秒.")


import asyncio
import itertools as it
import os
import random
import time

async def makeitem(size: int = 5) -> str:
    return os.urandom(size).hex()

async def randsleep(caller=None) -> None:
    i = random.randint(0, 10)
    if caller:
        print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)

async def produce(name: int, q: asyncio.Queue) -> None:
    n = random.randint(0, 10)
    for _ in it.repeat(None, n):  # Synchronous loop for each single producer
        await randsleep(caller=f"Producer {name}")
        i = await makeitem()
        t = time.perf_counter()
        await q.put((i, t))
        print(f"Producer {name} added <{i}> to queue.")

async def consume(name: int, q: asyncio.Queue) -> None:
    while True:
        await randsleep(caller=f"Consumer {name}")
        i, t = await q.get()
        now = time.perf_counter()
        print(f"Consumer {name} got element <{i}>"
              f" in {now-t:0.5f} seconds.")
        q.task_done()

async def main(nprod: int, ncon: int):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
    await asyncio.gather(*producers)
    await q.join()  # Implicitly awaits consumers, too
    for c in consumers:
        c.cancel()

if __name__ == "__main__":
    import argparse
    random.seed(444)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--nprod", type=int, default=5)
    parser.add_argument("-c", "--ncon", type=int, default=10)
    ns = parser.parse_args()
    start = time.perf_counter()
    asyncio.run(main(**ns.__dict__))
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")
