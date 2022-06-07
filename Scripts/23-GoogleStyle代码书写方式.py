#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : Scripts/23-GoogleStyle代码书写方式.py
# @Info        : 
# @Last Edited : 2022-06-07 11:19:15

"""Google 样式的 docstring 示例.

所谓 docstring, 对于 Python 而言, 是指在代码文件开头的三引号之间的内容. 
内容通常描述了该模块的功能, 功能示例, 属性列表以及逻辑说明等等.
由于中英文的差异, 我这里除了遵循原文档的格式之外, 内容上加了许多我自己的理解.

这个模块演示了 `Google Python Style Guide`_ 的 docstring 书写风格. 文档字符串可以跨越多行. 
一个 Section 通常这样书写: `小节标题` 后跟着 `半角英文冒号`, 另起一行缩进之后, 继续写剩下的文本.
文档及代码中的所有标点符号, 均使用英文半角, 而不用中文标点符号.
标点符号之后空一格, 中英文之间空一格, 反引号括起来的内容前后空一格.

Example:
    示例的标题可以为 ``Example`` 或者 `Examples`.
    在这里的缩进部分, 支持书写任何形式的内容, 不会被渲染成其他格式.
    很适合书写 reStructuredText::

        $ python example_google.py

当新的内容不再延续之前的缩进, 开始顶格写时, 会创建 Section breaks (分节符), 此时的内容属于另一个 Section.
每当新的 Section 开始时, 也会隐式地创建 Section breaks. 

Attributes:
    module_level_variable1 (int): 模块级别的变量可以记录在 docstring 中的 Attributes Section 中, 或者
        后面的内联文档中 (下面会演示), 紧跟在变量后面.

        两种形式都可以, 但不要混用, 选择其中一种, 并一以贯之.

Todo:
    * 这里 TODOs 模块会用到
    * 并且需要用到 ``sphinx.ext.todo`` 插件

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

module_level_variable1 = 12345

module_level_variable2 = 98765
"""int: 这里就是模块级别变量内联文档.

这里的内容也可以跨越多行.
可以选择在第一行指定类型，用冒号分隔。
"""


def function_with_types_in_docstring(param1, param2):
    """函数的 docstring 示例.

    支持 `PEP 484`_ 类型注释. 如果属性、参数和返回类型根据 `PEP 484`_ 进行
    注释, 则它们不需要包含在 docstring 中:

    Args:
        param1 (int): 第一个参数.
        param2 (str): 第二个参数.

    Returns:
        bool: 返回值. True 表示成功, False 表示其他情况.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """


def function_with_pep484_type_annotations(param1: int, param2: str) -> bool:
    """PEP 484 风格的函数 docstring 示例.

    和上面的例子不同的是, 行参后面标了参数类型, 而且在函数末尾标明了返回值类型.

    Args:
        param1: 第一个参数.
        param2: 第二个参数.

    Returns:
        返回值. True 表示成功, False 表示其他情况.

    """


def module_level_function(param1, param2=None, *args, **kwargs):
    """模块级别函数的 docstring 示例.

    函数参数应记录在 ``Args`` Section 中. 每个参数名称都要写清楚.
    参数类型和参数描述不强制要求写明, 但如果不明显, 最好写上.

    如果允许接收不定参数 \*args 或者 \*\*kwargs, 应该这样写: ``*args`` and ``**kwargs``.

    参数的格式为::

        name (type): description
            参数描述可以跨越多行.
            后面的行要缩进. `(type)` 可以不写.

            参数描述可以分多个段落。

    Args:
        param1 (int): 第一个参数.
        param2 (:obj:`str`, optional): 第二个参数. 默认为 None.
            描述的第二行应该缩进.
        *args: 列表参数.
        **kwargs: 字典参数.

    Returns:
        bool: True 表示成功, False 表示其他情况.
        
        返回类型可以不写, 可以在 ``Returns`` Section 的开头指定, 后跟英文半角冒号.

        ``Returns`` Section 可以跨越多行和多段.
        后面的行也应缩进, 与第一行的样式匹配.

        ``Returns`` Section 支持书写 reStructuredText.
        包括代码片段::

            {
                'param1': param1,
                'param2': param2
            }

    Raises:
        AttributeError: ``Raises`` Section 是与接口相关的所有异常的列表。
        ValueError: 如果 `param2` 与 `param1` 相等.

    """
    if param1 == param2:
        raise ValueError('param1 may not be equal to param2')
    return True


def example_generator(n):
    """生成器函数没有 ``Returns`` Section, 而是 ``Yields`` Section.

    Args:
        n (int): 生成器的范围, 从 0 到 `n` - 1.

    Yields:
        int: 0 到 `n` - 1 范围的下一个数字.

    Examples:
        Examples Section 应以 doctest 格式编写，并应说明如何使用该功能。

        >>> print([i for i in example_generator(4)])
        [0, 1, 2, 3]

    """
    for i in range(n):
        yield i


class ExampleError(Exception):
    """异常的记录方式与类相同.

    __init__ 方法可以记录在类级别的 docstring 中, 也可以记录
    在 __init__ 方法本身的 docstring 中。

    两种形式都可以, 但不要混用, 选择其中一种, 并一以贯之.

    Note:
        不要在 ``Args`` Section 中包含 `self` 参数.

    Args:
        msg (str): 异常描述, 尽量通俗易懂.
        code (:obj:`int`, optional): 错误状态码.

    Attributes:
        msg (str): 异常描述, 尽量通俗易懂.
        code (int): 错误状态码.

    """

    def __init__(self, msg, code):
        self.msg = msg
        self.code = code


class ExampleClass(object):
    """类的 docstring 的摘要尽量用一行描述清楚.

    如果该类具有公共属性, 将他们写在 ``Attributes`` Section 中, 格式与 ``Args`` 相同.
    或者也可以写在属性声明中 (参见下面的 __init__ 方法).

    使用 ``@property`` 装饰器创建的属性应该记录在属性的 getter 方法中.

    Attributes:
        attr1 (str): 属性 `attr1` 的描述.
        attr2 (:obj:`int`, optional): 属性 `attr2` 的描述.

    """

    def __init__(self, param1, param2, param3):
        """__init__ 方法的 docstring 示例.

        __init__ 方法可以记录在类级别的文档字符串中, 也可以记录在 __init__ 方法本身的文档字符串中.

        两种形式都可以, 但不要混用, 选择其中一种, 并一以贯之.

        Note:
            不要在 ``Args`` Section 中包含 `self` 参数.

        Args:
            param1 (str): 参数 `param1` 的描述.
            param2 (:obj:`int`, optional): 参数 `param2` 的描述. 支持
                多行.
            param3 (:obj:`list` of :obj:`str`): 参数 `param3` 的描述.

        """
        self.attr1 = param1
        self.attr2 = param2
        self.attr3 = param3  #: 属性的 *行内* 注释

        #: list of str: 属性的 *行前* 注释, 标明属性类型
        self.attr4 = ['attr4']

        self.attr5 = None
        """str: 属性的 *行后* 注释, 标明属性类型."""

    @property
    def readonly_property(self):
        """str: 属性应记录在其 getter 方法中."""
        return 'readonly_property'

    @property
    def readwrite_property(self):
        """:obj:`list` of :obj:`str`: 同时具有 getter 和 setter 的属性只应记录在其 getter 方法中.

        如果 setter 方法包含显著行为, 则应在此处提及.
        """
        return ['readwrite_property']

    @readwrite_property.setter
    def readwrite_property(self, value):
        value

    def example_method(self, param1, param2):
        """类方法类似于常规函数.

        Note:
            不要在 ``Args`` Section 中包含 `self` 参数.

        Args:
            param1: 参数 `param1` 的描述.
            param2: 参数 `param2` 的描述.

        Returns:
            True 表示成功, False 表示其他情况.

        """
        return True

    def __special__(self):
        """默认情况下, 特殊方法的 docstring 不会输出.

        特殊方法是以双下划线开头和结尾的任何方法或属性.
        要想输出这里的 docstring, 需要将 ``napoleon_include_special_with_doc`` 设置为 True.

        可以通过更改 Sphinx 的 conf.py 中的这个配置::

            napoleon_include_special_with_doc = True

        """
        pass

    def __special_without_docstring__(self):
        pass

    def _private(self):
        """默认情况下不包括私有方法.

        私有方法是以下划线开头并且*不是*特殊方法的任何方法或属性.
        默认情况下不会输出.

        可以通过更改 Sphinx 的 conf.py 中的这个配置::

            napoleon_include_private_with_doc = True

        """
        pass

    def _private_without_docstring(self):
        pass
