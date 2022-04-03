Linux 看 CPU 信息

```shell
cat /proc/cpuinfo | grep 'physical id' | sort | uniq | wc -l
```