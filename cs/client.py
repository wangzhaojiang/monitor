#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-11-01 18:13
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------
import socket
import os
from function import *



def client_socket():
    HOST = '127.0.0.1'
    PORT = 10000
    BUFSIZ = 512
    ADDR = (HOST, PORT)
    
    clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    clisock.connect(ADDR)

    data = getdata()

    data = str(data)

    clisock.send(data)

def getdata():
    # execute the __file__.py to get the monitor data
    cpu_data = cpu.main()
#    diskio_data = diskio.main()
#    flow_data = flow.main()
#    memory_data = memory.main()
#    netstat_data = netstat.main()

    data = {'cpu': cpu_data,
#            'diskio': diskio_data,
#            'flow': flow_data,
#            'memory': memory_data,
#            'netstat': netstat_data,
            }

    return data




if __name__ == '__main__':
    client_socket()
    
