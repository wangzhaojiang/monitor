#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-10-13 18:56
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------

import time
import re


def Download():




start = time.time()
old = open('/pro/net/dev', 'r')
byte_old = old.readlines()[2].split()[1]
old.close()
stop = time.time()
use_time = stop - start
