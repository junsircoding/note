"""
Python 正则测试用例
"""

import re
pattern = re.compile(ur'^[0-9]*$')
str = u'12345'
print(pattern.search(str))
