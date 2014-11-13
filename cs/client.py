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
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    
    clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    clisock.connect(ADDR)

    data = getdata()

    data = process_data(data)

    #clisock.send(data)

def process_data(data):
    host = socket.gethostname()
    ip = socket.gethostbyname(host)

    cpu_data = data['cpu']
    diskio_data = data['diskio']
    flow_data = data['flow']
    memory_data = data['memory']
    netstat_data = data['netstat']

    def tostr(data):
        count = 0
        while count < len(data):
            data[count] = str(data[count])
            count += 1

    tostr(cpu_data)
    tostr(diskio_data)
    tostr(flow_data)
    tostr(memory_data)
    tostr(netstat_data)
    
    cpu_data = 'cpu' + '^^' + '^^'.join(cpu_data) + '^^' + '|' + '^^'
    diskio_data = 'diskio' + '^^' + '^^'.join(diskio_data) + '^^' + '|' + '^^'
    flow_data = 'flow' + '^^' + '^^'.join(flow_data) + '^^' + '|' + '^^'
    memory_data = 'memory' + '^^' + '^^'.join(memory_data) + '^^' + '|' + '^^'
    netstat_data = 'netstat' + '^^' + '^^'.join(netstat_data) + '^^' + '|' + '^^'
    

    result = host + '^^' + ip + '^^' + cpu_data + diskio_data + flow_data + memory_data + netstat_data

    print result
    print len(result)

    return result



def getdata():
    # execute the __file__.py to get the monitor data
    
    #cpu_data = cpu.main()
    #diskio_data = diskio.main()
    #flow_data = flow.main()
    #memory_data = memory.main()
    #netstat_data = netstat.main()

    #data = {'cpu': cpu_data,
    #        'diskio': diskio_data,
    #        'flow': flow_data,
    #        'memory': memory_data,
    #        'netstat': netstat_data,
    #        }
    categoty = ['cpu', 'diskio', 'flow', 'memory', 'netstat']

    return data




if __name__ == '__main__':
    client_socket()
    
