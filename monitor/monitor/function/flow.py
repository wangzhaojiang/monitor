#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-10-21 18:09
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------
import re
import time


def getdata_flow():
    f = open('/proc/net/dev', 'r')
    content = f.readlines()
    f.close()

    del content[0]
    del content[0]

    data = []

    for each_line in content:
        each_line = each_line.split()
        result = [each_line[0], int(each_line[1]), int(each_line[2])]

        data.append(result)

    return data

def flow():
    data_old = getdata_flow()
    
    #time_old = time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time()))
    time.sleep(3)
    #time_new = time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time()))
    
    data_new = getdata_flow()

    result = []

    count = 0

    while count < len(data_old):
        old = data_old[count]
        new = data_new[count]
        interface = old[0]
        byte = new[1] - old[1]
        packets = new[2] - old[2]

        tmp = [interface, byte, packets]
        result.append(tmp)

        count += 1

    print result


flow()


