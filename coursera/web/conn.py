import socket
mysoc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sec = mysoc.connect(("www.google.com",90))