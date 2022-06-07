安装 JDK

1.下载压缩包安装 oracle Java JDK
华为镜像地址：

```shell
https://mirrors.huaweicloud.com/java/jdk/
```

2.解压缩到指定目录
创建目录:

```shell
sudo mkdir /usr/lib/jvm
```

解压缩到该目录:

```shell
sudo tar -zxvf jdk-7u60-linux-x64.gz -C /usr/lib/jvm
```

3.修改环境变量:　　

```shell
sudo vim ~/.bashrc
```

在文件末尾追加下面内容：

```shell
#set oracle jdk environment
export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_191  ## 这里要注意目录要换成自己解压的jdk 目录
export JRE_HOME=${JAVA_HOME}/jre  
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib  
export PATH=${JAVA_HOME}/bin:$PATH  
```

使环境变量马上生效：

```shell
source ~/.bashrc
```

4.系统注册此jdk

```shell
sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk1.8.0_191/bin/java 300
```

5.查看java版本，看看是否安装成功：

```shell
java -version
```

如果安装了多个版本的jdk，可以通过以下命令在这些版本之间切换：

```shell
sudo update-alternatives –config java
```

前面带星号的是当前正在使用的java版本，键入编号选择使用哪个版本。

![](https://p.qlogo.cn/qqmail_head/rwzOcu9uLseNKBm3MFXahbicUMCaTibSiaB6btK8y0oEJIARrdEgMwsAibovOyFu2OGyBicSHfNjfAro/0)
