Windows 10 安装 Windows Terminal

```powershell
# 安装 choco
@powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
# 用 choco 安装 Windows Terminal
choco install microsoft-windows-terminal
```