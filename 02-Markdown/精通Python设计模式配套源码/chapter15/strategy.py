#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding@gmail.com
# @File        : 02-Markdown/精通Python设计模式配套源码/chapter15/strategy.py
# @Info        : 
# @Last Edited : 2022-06-08 18:04:57

import time
SLOW = 3  # 单位为秒
LIMIT = 5   # 字符数
WARNING = 'too bad, you picked the slow algorithm :('


def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]


def allUniqueSort(s):
    if len(s) > LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    srtStr = sorted(s)
    for (c1, c2) in pairs(srtStr):
        if c1 == c2:
            return False
    return True


def allUniqueSet(s):
    if len(s) < LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    return True if len(set(s)) == len(s) else False


def allUnique(s, strategy):
    return strategy(s)


def main():
    while True:
        word = None
        while not word:
            word = input('Insert word (type quit to exit)> ')
            if word == 'quit':
                print('bye')
                return

            strategy_picked = None
            strategies = {'1': allUniqueSet, '2': allUniqueSort}
            while strategy_picked not in strategies.keys():
                strategy_picked = input('Choose strategy: [1] Use a set, [2] Sort and pair> ')

                try:
                    strategy = strategies[strategy_picked]
                    print('allUnique({}): {}'.format(word, allUnique(word, strategy)))
                except KeyError as err:
                    print('Incorrect option: {}'.format(strategy_picked))

if __name__ == '__main__':
    main()
