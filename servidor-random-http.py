#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Aplicación web que devuelve URLs aleatorias
"""

import random
import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 2525))

mySocket.listen(5)

try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'Request received:'
        print recvSocket.recv(2048)
        print 'Answering back...'
        randNumber = random.randint(1, 1000000)
        recvSocket.send('HTTP/1.1 200 OK\r\n\r\n' +
                        '<html><body>' +
                        '<p>Hola. ' +
                        '<a href="' + str(randNumber) + '">Dame otra</a></p>'
                        '</body></html>\r\n')
        recvSocket.close()

except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
