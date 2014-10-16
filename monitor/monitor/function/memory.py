#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-10-16 15:28
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------



def getdata_memory():
    f = open('/proc/meminfo', 'r')
    
    data = []
    num = 0 # 只读取前四行

    while num < 4:
        content = f.readline()
        content = content.split()

        content[1] = int(content[1])
        
        data.append(content[1])

        num += 1


    return data


def memory():
    """内存使用率(MEMUsedPerc)=100*(MemTotal-MemFree-Buffers-Cached)/MemTotal"""
    data = getdata_memory()

    MEMusePerc = (data[0] - data[1] - data[2] - data[3]) * 1.0 / data[0]

    return '{\"MemUse\": %s}' % MEMusePerc
