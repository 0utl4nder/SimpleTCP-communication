#!/usr/bin/python3

import socket

serverSocketObject = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

host = '192.168.0.4' # replace with ur local ip (ifconfig) or (hostname)
port = 444

serverSocketObject.bind((host, port))


# -TCP listener

serverSocketObject.listen(3)

while True:
    clientsocket, address = serverSocketObject.accept()

    print("Received connection from %r" % str(address))

    message = 'Connected to %r' % str(host) + '!!'
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
#By 0utl4nder
