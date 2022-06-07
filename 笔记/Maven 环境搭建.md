Maven 环境搭建

1. 下载 3.5.2 版本的 maven 源码

2. 环境变量里面添加 MAVEN_HOME，对应值填 maven 源码的 bin 目录

3. maven 的调用需要用到 JAVA_HOME，注意 JAVA_HOME 的环境变量值后面不要加分号，这个注意点仅限 win10。

4. 配置完之后，cmd 输入 mvn -v 测试如下即为成功

```shell
----------
Apache Maven 3.5.2 (138edd61fd100ec658bfa2d307c43b76940a5d7d; 2017-10-18T15:58:13+08:00)
Maven home: C:\Users\wangjun\Documents\maven_root\apache-maven-3.5.2\bin\..
Java version: 1.7.0_72, vendor: Oracle Corporation
Java home: C:\Program Files (x86)\Java\jdk1.7.0_72\jre
Default locale: zh_CN, platform encoding: GBK
OS name: "windows 8.1", version: "6.3", arch: "x86", family: "windows"
----------
```

如果出现这样

```shell
----------
The JAVA_HOME environment variable is not defined correctly
----------
```

这便是环境变量的问题