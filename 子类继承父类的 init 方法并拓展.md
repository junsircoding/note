子类继承父类的init方法并拓展（Python3）

```python
# super方式：

class P:
    """
    父类
    """
    def __init__(self, p1):
        self.p1 = p1
    
class C(P):
    """
    子类
    """
    def __init__(self, p1, p2):
        super(C, self).__init__(p1)
        self.p2 = p2


if __name__ == "__main__":
    c = C(
        p1="p1",
        p2="p2"
    )
    print(c.p1)
    print(c.p2)

# property方式：

class P:
    """
    父类
    """
    def __init__(self, p1):
        self.p1 = p1
    
class C(P):
    """
    子类
    """
    @property
    def p2(self):
        if "_p2" not in self.__dict__.keys():
            self.p2 = "p2"
            return self._p2
    @p2.setter
    def p2(self, value):
        self._p2 = value


if __name__ == "__main__":
    c = C(
        p1="p1"
    )
    print(c.p1)
    print(c.p2)
```