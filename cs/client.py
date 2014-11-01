#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-11-01 18:13
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------
import socket



def client_socket():
    HOST = '127.0.0.1'
    PORT = 10000
    BUFSIZ = 4096
    ADDR = (HOST, PORT)
    
    clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    clisock.connect(ADDR)

    data = getdata()

    clisock.send(data)

def getdata():
    pass

