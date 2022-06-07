递归删除所有pyc文件

```shell
find . -name "*.pyc" -type f -print -exec rm -rf {} \;
```