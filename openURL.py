#!/usr/bin/env python3
import socket
import webbrowser
"""A reciever of URLs. It opens them directly."""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 60606
s.bind(('0.0.0.0', port))
print (f'Socket binded to port {port}')
s.listen(3)
print ('socket is listening')
try:
    while True:
        c, addr = s.accept()
        print ('Got connection from ', addr)
        if addr[0].startswith('192.168.0.'):
            url = c.recv(1024).decode()
            print(f'Opening: "{url}"')
            webbrowser.open(url)
        c.close()
except KeyboardInterrupt:
    print('Shutting down...')
    s.shutdown(1)
    s.close()