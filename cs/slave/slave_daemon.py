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

os.chdir(os.path.dirname('./' + sys.argv[0]))
sys.path.append('..')

from get_conf import *


def cli():

    alive_log = open('../logs/slave_alive.log', 'a+')
    send_log = open('../logs/send_data.log', 'a+')
    print os.getcwd()

    os.chdir('../')
    param = get_conf_data()
    BUFSIZE = 1024
    HOST = param['master_node']
    PORT = int(param['daemon_port'])
    ADDR = (HOST, PORT)
    print ADDR

    os.chdir('slave/')

    udp_cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        time_now = time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time()))
        udp_cli.sendto('online', ADDR)
        print 'send online info'
        time_now = time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time()))
        print >> send_log, time_now, ' send data to ',param['master_node'], '(master)'
        data, addr = udp_cli.recvfrom(BUFSIZE)
        print >> alive_log, time_now, ' ', addr[0], '(master)', 'is alive'
        os.system('python slave.py')
cli()
