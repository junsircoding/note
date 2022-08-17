#!/bin/bash 
# set -x
# 获取当前时间, 并格式化 
echo `date "+%Y%m%d%H%M"` 
# 202208111428 

# 时间加一天 
echo `date --date "+1 day" "+%Y%m%d%H%M"` 

# 时间加一分钟 
echo `date --date "+1 min" "+%Y%m%d%H%M"` 

# 获取指定月份的第一天和最后一天
# 首个参数不传置为当天日期
if [ "x$1" == "x" ] ; then
    #date=$(whichtime3 glb)
    date_m=$(date +%Y%m)
else
    date_m=$1
fi
date_m=202206
date_m_1=`date -d "${date_m:0:6}01 +1 month" +%Y%m%d`
echo $date_m_1
# 指定月首日
first_d=${date_m:0:6}01
echo $first_d
first_d_1=${date_m_1:0:6}01
echo $first_d_1
# 指定月末日
last_d=`date -d "${first_d_1:0:6}01 -1 day" +%Y%m%d`
echo $last_d

echo $date_m"首日:"$first_d", 末日:"$last_d