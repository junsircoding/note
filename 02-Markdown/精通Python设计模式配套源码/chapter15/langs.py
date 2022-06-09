#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding@gmail.com
# @File        : 02-Markdown/精通Python设计模式配套源码/chapter15/langs.py
# @Info        : 
# @Last Edited : 2022-06-09 14:57:29

import pprint
from collections import namedtuple
from operator import attrgetter
if __name__ == '__main__':
    ProgrammingLang = namedtuple('ProgrammingLang', 'name ranking')
    stats = (('Ruby', 14), ('Javascript', 8), ('Python', 7),
             ('Scala', 31), ('Swift', 18), ('Lisp', 23))
    lang_stats = [ProgrammingLang(n, r) for n, r in stats]
    pp = pprint.PrettyPrinter(indent=5)
    pp.pprint(sorted(lang_stats, key=attrgetter('name')))
    print()
    pp.pprint(sorted(lang_stats, key=attrgetter('ranking')))
