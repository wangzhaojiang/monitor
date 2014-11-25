#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-11-24 14:01
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------
from get_conf import *
import socket
import os


def check():
    data = get_conf_data()
    
    #check the MySQLdb
    try:
        import MySQLdb

    except:
        #install MySQLdb
        print 'install MySQLdb'

    #get local ip
    localip = socket.gethostbyname(socket.gethostname())

    if(localip == data['master_node']):
        print 'MASTER:...'
        #master do
        os.system('python master/master_daemon.py')


    else:
        print 'Slave...'
        #slave do
        os.system('python slave/slave_daemon.py')


check()
