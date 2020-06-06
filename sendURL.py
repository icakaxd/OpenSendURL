#!/usr/bin/env python3
import sys
import socket
import appex

if appex.get_url():
	url = appex.get_url()
elif sys.argv[1]:
	url = sys.argv[1]
else:
	url = input()

s = socket.socket()
s.connect(('192.168.0.100', 60606))
s.sendall(url.encode())
s.close()