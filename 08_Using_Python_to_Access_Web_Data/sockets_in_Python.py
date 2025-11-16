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


file = open('mbox-short.txt', 'rw')
data = file.encode()

print(data[:500])