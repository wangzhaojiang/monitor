#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-10-14 21:03
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------

import re
import os


content = os.popen('netstat -tunlp').readlines()

del content[0]
del content[1]

results = []

for each_line in content:
    each_line = each_line.split()
    if 'LISTEN' in each_line:
        each_line.remove('LISTEN')

    stat = []
    
    stat.append(each_line[0])
    stat.append(each_line[3])
    stat.append(each_line[5])

    results.append(stat)

print results
