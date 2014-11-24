#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-11-24 14:01
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------
from get_conf import *
import socket


def check():
    data = get_conf_data()

    #get local ip
    localip = socket.gethostbyname(socket.gethostname())

    if(localip == data['master_node']):
        print 'MASTER:...'
        #master do
        pass

    else:
        print 'Slave...'
        #slave do
        pass


check()
