#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding@gmail.com
# @File        : 13-miniweb_1/startServer.py
# @Info        : 
# @Last Edited : 2022-06-09 14:57:29

# 用多线程的方式创建TCP服务器
# 目标：运行代码，服务器开启，在浏览器输入localhost:8341进入主页
# 导包
import socket
import threading
import application


def handle_connect(server_client_socket):
    # 接收请求报文
    request_data = server_client_socket.recv(4096)
    # 判断请求报文是否为空，若为空则判定客户端中断连接，程序停止
    if not request_data:
        print('客户端退出连接！')
        server_client_socket.close()
        return
    # 请求报文不为空，打印请求报文
    # print('请求报文为：', request_data.decode())
    # 处理请求报文，获取请求资源名称
    file_name = request_data.split()[1].decode()
    print('请求资源：', file_name)

    # 对“客户端访问不存在的页面”这种情况做容错处理
    if file_name == '/':
        file_name = '/index.html'

    if file_name.endswith('.html'):
        env = {'file_name': file_name}
        # 构造响应报文
        # 构造响应行，记住加\r\n
        response_line = 'Http/1.1 200 ok\r\n'
        # 构造响应头，记住加\r\n
        response_head = 'Server:MiniWeb/1.0\r\n'
        # 构造响应体
        response_body = application.app(env)
        # 发送响应报文
        response_data = (response_line + response_head + '\r\n').encode() + response_body.encode()
        server_client_socket.send(response_data)
        server_client_socket.close()
    else:
        try:
            with open('static' + file_name, 'rb') as f:
                file_data = f.read()
        except FileNotFoundError as e:
            # 读取404页面信息
            with open('static/error.html', 'rb') as f:
                file_data = f.read()

        # 构造响应报文
        # 构造响应行，记住加\r\n
        response_line = 'Http/1.1 200 ok\r\n'
        # 构造响应头，记住加\r\n
        response_head = 'Server:MiniWeb/1.0\r\n'
        # 构造响应体
        response_body = file_data
        # 发送响应报文
        response_data = (response_line + response_head + '\r\n').encode() + response_body
        server_client_socket.send(response_data)
        server_client_socket.close()


def main():
    # 创建socket，参数为ipv4，字节流
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用，参数为当前socket，设置端口复用
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定ip
    server_socket.bind(('', 8351))
    # 开启监听
    server_socket.listen(128)

    while True:
        try:
            # 接收连接
            server_client_socket, server_client_ip_port = server_socket.accept()
            print(server_client_ip_port, 'connect success...')
        except KeyboardInterrupt as e:
            print('服务器关闭，程序退出!')
            break

        # 收发数据，使用线程
        sub_thread = threading.Thread(target=handle_connect, args=(server_client_socket,))
        sub_thread.start()
        # 关闭连接，因为不会执行，所以省略


if __name__ == '__main__':
    main()
