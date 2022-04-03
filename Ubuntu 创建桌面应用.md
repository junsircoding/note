Ubuntu 创建桌面应用

```shell
cd /usr/share/applications
```

新建文件 `.desktop`

内容为：

```shell
[Desktop Entry]
Name=应用名
Comment=应用描述
GenericName=Markdown Editor
Exec=应用绝对路径
Icon=图标绝对路径
Type=Application
StartupNotify=true
Categories=Office;WordProcessor;
MimeType=text/markdown;text/x-markdown;
```

其他随便填

```shell
cd /usr/bin
```

建立硬链接

```shell
sudo ln 应用绝对路径
```