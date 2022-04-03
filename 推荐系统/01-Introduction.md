# 课程简介

### 1. 课程安排

第一天： Flask-RESTful + 项目介绍 + 数据库设计
第二天： 数据库方案 + Gitflow工作流
第三天： 认证方案
第四天： 缓存方案
第五天： RPC方案 grpc
第六天： 搜索方案
第七天： 即时通讯方案

### 2. 目标

* 以黑马头条产品为依托案例，但不再以具体业务实现为主
* 力求掌握解决不同问题的实施方案
* 深入理解并巩固前面所学的知识

### 3. 学习方法

* 尽量不要死记硬背，要去理解问题和方法的本质
* 多思考**做了什么**和**为什么**
* 自己能把自己讲明白

### 4. 见谅

刚从开发线上下来，文档还不能算是课件，恳请谅解。

### 5. 虚拟机说明

* CentOS7.2

* 黑窗口 无GNOME

* 用户名 密码

  * 系统
    * root  -> chuanzhi
    * python -> chuanzhi
  * MySQL
    * root -> mysql

* 端口

  * MySQL (mariadb)
    * master -> 3306
    * slave -> 8306   (mysql -uroot -p -h 127.0.0.1 --port=8306)
  * Redis
    * cluster  -> 7000  7001 7002 7003 7004 7005
    * master & slave -> 6380 6381
    * sentinel -> 26380 26381 26382
  * Elasticsearch 5
    * 9200

* Python 虚拟环境 

  * workon toutiao

* 关机 sudo shutdown now

* 重启 reboot

  