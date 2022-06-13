#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding@gmail.com
# @File        : 14-miniweb_2/HttpServer.py
# @Info        : 
# @Last Edited : 2022-06-13 11:11:05

# 构造HTTP服务器类
import socket
import threading
import sys
import Applicaton


class HttpServer(object):
    # 构造初始化方法
    def __init__(self, port):
        # 创建服务器socket，参数为ipv4，字节流
        self.s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置服务器socket端口可以复用，参数为此socket，可复用，true
        self.s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定ip和端口，注意是元组，ip写为空串，表示本机所有ip均可以被访问
        self.s_socket.bind(('', port))
        # 变主动为被动，开启监听，监听数为128个
        self.s_socket.listen(128)

    def start(self):
        # 循环
        while True:
            # 接收客户端连接，拆包获取服务器-客户端socket，ip_port元组
            try:
                s_c, ip_port = self.s_socket.accept()
                sub_thread = threading.Thread(target=self.handle_customer, args=(s_c,))
                sub_thread.daemon = True
                sub_thread.start()
            except KeyboardInterrupt as e:
                print('服务器关闭!')
                self.s_socket.close()
                sys.exit()

    def handle_customer(self, s_c):
        # 构造子线程处理客户端连接方法
        # 接收请求报文，获取客户端要请求的资源
        request_message = s_c.recv(4096)
        # 处理请求报文，获取客户端请求的资源
        file_name = request_message.decode().split()[1]
        # 构造响应报文
        if file_name == '/':
            file_name = '/index.html'
        if file_name.endswith('.html'):
            # 将请求报文传给框架，返回响应报文
            source_action = {'file_name': file_name}
            response_line = 'HTTP/1.1 200 ok\r\n'
            response_head = 'Server:MiniWeb2\r\n'
            response_body = Applicaton.app(source_action)
            response_message = (response_line + response_head + '\r\n').encode() + response_body.encode()
            s_c.send(response_message)
        else:
            try:
                with open('static' + file_name, 'rb') as f:
                    response_body = f.read()
                response_line = 'Http 200 ok\r\n'
                response_head = 'Server:MiniWeb2\r\n'
                response_message = (response_line + response_head + '\r\n').encode() + response_body
                s_c.send(response_message)
            except FileNotFoundError as e:
                with open('static/error.html', 'rb') as f:
                    response_body = f.read()
                response_line = 'Http 404 not found\r\n'
                response_head = 'Server:MiniWeb2\r\n'
                response_message = (response_line + response_head + '\r\n').encode() + response_body
                s_c.send(response_message)
            finally:
                s_c.close()


# 构造main方法
def main():
    # 构造命令行方式启动
    # 判断命令行中接收的是否为两个参数
    # if len(sys.argv) != 2:
    #     return
    # # 判断第二个参数是否为纯属数字
    # if not sys.argv[1].isdigit():
    #     return
    # # 获取输入的端口号，并将其类型转换为int
    # port = int(sys.argv[1])

    # 创建server对象，将端口号作为参数传入
    server_o = HttpServer(7856)
    server_o.start()


# 构造全局main测试入口方法
if __name__ == '__main__':
    main()
