# -*- coding:utf-8 -*-
__author__ = 'shichao'

import socket
import threading
import time
import cv2


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        print(data)
        # cv2.imshow('recv img',data)
        # cv2.waitKey(10000)
        # cv2.destroyAllWindows()
        # time.sleep(1)
        # if not data or data.decode('utf-8') == 'exit':
        #     break
        sock.send(data)
        # print(('server Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
        # sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
    exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')

while True:
    # 接手一个新连接:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
