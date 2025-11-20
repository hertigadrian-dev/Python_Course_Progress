# import socket

# phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# data = phone.connect_ex(('data.pr4e.org', 80))

# if data != 0:
# 	print('connection failed! error code:', data)
# 	exit()

# my_request = (
# 	'GET /romeo.txt HTTP/1.1\r\n'
# 	'Host: data.pr4e.org\r\n'
# 	'Connection: close\r\n'
# 	'\r\n'
# 	).encode()

# phone.send(my_request)

# while True:
# 	ceva = phone.recv(500)
# 	if len(ceva) < 1:
# 		break
# 	print(phone.decode())
# phone.close()


#------------------------
''' Shorter version '''
'''   No Headers   ''' 
#------------------------
#ex.1
# import socket 
# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
# 	print(line.decode().strip())

#ex.2
import socket 
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
adri = {}
for line in fhand:
	words = line.decode().split()
	for stuff in words:
		adri[stuff] = adri.get(stuff, 0) + 1
print(max(adri))






