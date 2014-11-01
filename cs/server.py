#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-11-01 17:39
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------

import socket
import threading
import MySQLdb


def server_socket():
    HOST = ''
    PORT = 10000
    BUFSIZ = 4096
    ADDR = (HOST, PORT)

    sersock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sersock.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
    sersock.bind(ADDR)
    sersock.listen(5)

    while True:
        print 'Waiting for the connection ...'
        clisock, addr = sersock.accept()
        print 'connection from :', addr
    
    try:
        data = clisock.recv(BUFSIZ)
        host = clisock.getpeername()
        thread = process(host, data)
        thread.start()
        clisock.close()
    
    except:
        print 'ERROR'
    

class process(threading.Thread):
    def __init__(self, host, data):
        threading.Thread.__init__(self)
        
        print 'processint host: %s monitor data' % host
        
        self.data = data
        self.host = host

    def run(self):
        'PROCESSING ...'
        pass
        #print 'HOST %s IS DONE' % host
        

if __name__ == '__main__':
    server_socket()
