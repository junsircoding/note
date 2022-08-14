#!/bin/bash 

# 获取当前时间, 并格式化 
echo `date "+%Y%m%d%H%M"` 
# 202208111428 

# 时间加一天 
echo `date --date "+1 day" "+%Y%m%d%H%M"` 

# 时间加一分钟 
echo `date --date "+1 min" "+%Y%m%d%H%M"` 