#!/usr/bin/env python3
"""A client for sending URLs to my PC."""
import socket
import sys

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 60606  # The port used by the server

if len(sys.argv) == 1:
    url = input("Please enter a URL. http(s)://")
else:
    url = sys.argv[1]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes(url, 'utf-8'))
    data = s.recv(1024)

print('Received', repr(data.decode('utf-8')))
