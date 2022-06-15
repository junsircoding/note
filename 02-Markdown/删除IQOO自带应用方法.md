# 卸载 IQOO 自带应用方法

1. MacOS 安装 adb 工具
   ```shell
   brew install --cask android-platform-tools
   ```
2. USB 连接手机, 打开 USB 调试等选项
3. 使用命令删除
   ```shell
   # 查看是否抓到设备
   adb devices
   # 进入 ADB Shell 环境
   adb shell
   # 列出当前所有应用包
   pm list packages
   # 卸载软件
   pm uninstall --user 0 com.package.name
   ```

# 进入调试模式

1. 关机
2. 音量+ & 电源
3. 相关命令
   ```shell
   adb reboot bootloader
   fastboot devices
   fastboot bbk unlock_vivo
   fastboot reboot
   ```