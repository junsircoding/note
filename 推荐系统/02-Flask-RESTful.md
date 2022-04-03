# Flask-RESTful

## 1. Flask 1.0 变化

### 开发模式的运行方式改变

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
  
  
  app.run(debug=True)

```

### 运行

```shell
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

### 说明

* 环境变量 FLASK_APP 指明flask的启动实例
* `flask run -h 10.211.55.5 -p 8000` 绑定地址 端口
* `flask run --help`获取帮助



* 环境变量
  * 操作系统保存的变量值
  * 通过export 声明
  * 通过echo $变量名 获取

### 扩展 

开发调试模式

```shell
$ export FLASK_ENV=development
$ flask run
```

* 默认生产模式 `FLASK_ENV=production`

## 2. 虚拟机使用演示

* 本地开发
* 远程运行

## 3. Flask-RESTful

明确学习Web框架的最基本目标：

1. 如何编写试图
2. 如何处理请求
3. 如何构造响应

<https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api>







