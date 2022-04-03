"""
在 flask 服务启动时异步执行定时任务
"""

# 1. flask 服务
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()
