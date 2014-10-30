#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-10-30 21:06
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------

import socket
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.setsockopt()
