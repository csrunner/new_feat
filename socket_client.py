# -*- coding:utf-8 -*-
__author__ = 'shichao'

import socket
import cv2
img = cv2.imread('/Users/shichao/Downloads/1.jpg')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
# for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    # s.send(data)
    # print(s.recv(1024).decode('utf-8'))

s.send(img)
blue = s.recv(1024)
# print(blue.shape)
# cv2.imshow('client win',blue)
# cv2.waitKey(10000)
# cv2.destroyAllWindows()
s.send(b'exit')
s.close()
