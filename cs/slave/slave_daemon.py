#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-11-23 22:54
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------
import socket
import os
import sys
import time

sys.path.append('..')

from get_conf import *


def cli():
    param = get_conf_data()
    BUFSIZE = 1024
    HOST = param['master_node']
    PORT = int(param['daemon_port'])
    ADDR = (HOST, PORT)
    print ADDR

    alive_log = open('../logs/slave_alive.log', 'a+')

    udp_cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        time_now = time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time()))
        udp_cli.sendto('online', ADDR)
        data, addr = udp_cli.recvfrom(BUFSIZE)
        print >> alive_log, time_now, ' ', addr[0], '(master)', 'is alive'
        os.system('python slave.py')
        time_now = time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time()))
        send_log = open('../logs/send_data.log', 'a+')
        print >> send_log, time_now, ' send data to ', addr[0]
cli()
