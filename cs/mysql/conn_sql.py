#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-11-25 21:25
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------
import MySQLdb

def conn():
    try:
        conn = MySQLdb.connect(user = 'root', db = 'monitor', passwd = 'notamaiba', host = 'localhost')
        cursor = conn.cursor()

        print 'connect sql suceed'
    except :
        print 'SQL connect ERROR...'

    return cursor

if __name__ == '__main__':
    conn()
