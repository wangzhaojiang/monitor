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



HOST = ''
PORT = 10000
BUFSIZ = 4096
ADDR = (HOST, PORT)


def server_socket():

    global HOST
    global PORT
    global BUFSIZ
    global ADDR

    sersock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sersock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sersock.bind(ADDR)
    sersock.listen(5)

    while True:
        print 'Waiting for the connection ...'
        clisock, addr = sersock.accept()
        print 'connection from :', addr
    
        
        #try:
        thread = process(clisock)
        thread.start()
        clisock.close()
        
        #except:
            #print 'ERROR'
    

class process(threading.Thread):
    def __init__(self, clisock):
        
        global BUFSIZ

        self.clisock = clisock
        self.data = self.clisock.recv(BUFSIZ)
        self.host = self.clisock.getpeername()

        threading.Thread.__init__(self)
        

    def run(self):
        'PROCESSING ...'
        #pass
        print 'processint host: ', self.host

        print self.data
        

if __name__ == '__main__':
    server_socket()
