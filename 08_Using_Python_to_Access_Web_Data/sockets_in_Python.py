# import socket #This module allows your program to communicate over the internet (TCP, UDP, etc.).

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPv4 / SOCK_STREAM = TCP / socket.socket(...) - Creates a “network connection object” 

# mysock.connect(('data.pr4e.org', 80))

# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
# 	data = mysock.recv(512)
# 	if (len(data) < 1):
# 		break
# 	print (data.decode())
# mysock.close()



import socket 

canal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
canal.connect(('data.pr4e.org', 80))


cmd = (
	'GET /romeo.txt HTTP/1.1\r\n'
	'Host: data.pr4e.org\r\n' 
	'Connection: close\r\n'
	'\r\n'

).encode()

canal.send(cmd)

while True:
	data = canal.recv(1000)
	if len(data) < 1:
		break
	print(data.decode())

canal.close()

#---------------------------

import socket 

canal = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # I am creating a network connection pipe using IPv4 and TCP
canal.connect(('data.pr4e.org', 80)) # opens a TCP connection to Hostname: data.pr4e.org and Port: 80

cmd = (
	'GET /romeo.txt HTTP/1.1\r\n'
	'Host: data.pr4e.org\r\n'
	'Connection: close\r\n'
	'\r\n'
	).encode()

canal.send(cmd)













