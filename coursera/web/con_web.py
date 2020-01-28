# import socket

# myso = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# myso.connect(('www.coursera.org',80))
# cmd = "GET https://www.coursera.org/learn/python-network-data/lecture/E4vSF/worked-example-sockets-chapter-12 HTTP/1.1\r\n\r\n".encode()
# myso.send(cmd)

# while (True):
#     data= myso.recv(512)
#     if(len(data) < 1):
#         break
#     print(data.decode())

# myso.close()

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
