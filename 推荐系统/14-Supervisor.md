# 进程管理 Supervisor

supervisor是进程管理工具

### 安装

```shell
sudo yum install python-pip     # python2 pip   apt-get
```

```shell
ps  查看进程  ps aux | grep xxx
netstat  查看端口  netstat -apn | grep 8000
tail 从文件末尾往前查看   tail -n 100 xxx      tail -f xxx
ssh
cat
chmod +x main.sh 改变权限
chown 改变文件拥有者
chgrp 改变用户组
less   less xxxx  more
tar
wget
grep  find  sed awk
scp  
kill
vi   # vim


crontab
```



**supervisor对python3支持不好，须使用python2**

```bash
sudo pip install supervisor
```

### 配置

运行**echo\_supervisord\_conf**命令输出默认的配置项，可以如下操作将默认配置保存到文件中

```bash
echo_supervisord_conf > supervisord.conf
```

vim 打开编辑supervisord.conf文件，修改

```bash
[include]
files = relative/directory/*.ini
```

为

```bash
[include]
files = /etc/supervisor/*.conf
```

include选项指明包含的其他配置文件。

将编辑后的supervisord.conf文件复制到/etc/目录下

```bash
sudo cp supervisord.conf /etc/
```

然后我们在/etc目录下新建子目录supervisor（与配置文件里的选项相同），并在/etc/supervisor/中新建tuotiao管理的配置文件toutiao.conf。

```
[group:toutiao]
programs=toutiao-app

[program:toutiao-app]
command=/home/python/scripts/toutiao_app.sh
directory=/home/python/toutiao-backend
user=python
autorestart=true
redirect_stderr=false
loglevel=info
stopsignal=KILL
stopasgroup=true
killasgroup=true

[program:apscheduler]
command=/home/python/scripts/apscheduler.sh
directory=/home/python/toutiao-backend
user=python
autorestart=true
redirect_stderr=false
loglevel=info
stopsignal=KILL
stopasgroup=true
killasgroup=true

[program:im]
command=/home/python/scripts/im.sh
directory=/home/python/toutiao-backend
user=python
autorestart=true
redirect_stderr=false
loglevel=info
stopsignal=KILL
stopasgroup=true
killasgroup=true
```

### 启动

```bash
supervisord -c /etc/supervisord.conf
```

查看 supervisord 是否在运行：

```bash
ps aux | grep supervisord
```

### supervisorctl

我们可以利用supervisorctl来管理supervisor。

```bash
supervisorctl

> status    # 查看程序状态
> start apscheduler  # 启动 apscheduler 单一程序
> stop toutiao:*   # 关闭 toutiao组 程序
> start toutiao:*  # 启动 toutiao组 程序
> restart toutiao:*    # 重启 toutiao组 程序
> update    ＃ 重启配置文件修改过的程序
```

执行status命令时，显示如下信息说明程序运行正常：

```bash
supervisor> status
toutiao:toutiao-app RUNNING pid 32091, uptime 00:00:02
```















