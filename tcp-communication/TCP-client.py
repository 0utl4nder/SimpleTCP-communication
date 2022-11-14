#!/usr/bin/python3

import socket

clientSocketObject = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

host = socket.gethostname()
port = 444
#                           ↓ replace   with ur local ip
clientSocketObject.connect(('192.168.0.4', port))

message = clientSocketObject.recv(1024)

clientSocketObject.close()
print(message.decode('ascii'))

