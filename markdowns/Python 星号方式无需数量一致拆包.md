Python 星号方式无需数量一致拆包

```python
In [1]: a,*b,c = [1,2,3,4]

In [2]: a
Out[2]: 1

In [3]: b
Out[3]: [2, 3]

In [4]: c
Out[4]: 4
```