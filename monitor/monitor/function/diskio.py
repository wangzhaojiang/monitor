#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-10-20 22:08
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------
import re
import time


def getdata_diskio():
    f = open('/proc/vmstat', 'r')
    content = f.readlines()

    option = ['^pgpgin', '^pgpgout']

    data = {}

    for each_line in content:
        for search in option:
            result = re.findall(search, each_line)
            if len(result) != 0:
                result = each_line.split()
                print result

                data[result[0]] = int(result[1])
                
                break

    return data


def diskio():
    data = getdata_diskio()
    print data


diskio()
