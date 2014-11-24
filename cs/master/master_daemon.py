#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-11-24 16:22
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------
import socket
import sys
import os
import time

sys.path.append('..')

from get_conf import *



def ser():
    param = get_conf_data()
    BUFSIZE = 1024
    HOST = ''
    PORT = int(param['daemon_port'])
    ADDR = (HOST, PORT)
    
    log = open('../logs/master_alive.log', 'a+')
    os.system('python master.py > /dev/null &')

    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sock.bind(ADDR)

    slaves = param['slave_node']

    while True:
        time_now = time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time()))
        data, addr = udp_sock.recvfrom(BUFSIZE)
        print >> log, time_now, ' ',  addr[0], ' is alive'
        udp_sock.sendto('got it', addr)    

ser()
