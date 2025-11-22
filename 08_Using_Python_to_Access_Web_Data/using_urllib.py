#----------------------
# Example using urllib
#----------------------

#ex
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
adri = {}
for line in fhand:
	words = line.decode().split()
	for stuff in words:
		adri[stuff] = adri.get(stuff, 0) + 1
print(max(adri))

#-------------------------



# ex.1

import getpass
import urllib.request, urllib.parse, urllib.error

#---------------------
# Passord Protection
#---------------------

def get_pass():
	parola = 'lol123'
	tries = 0

	while tries < 3:
		user = getpass.getpass('insert your password: ')

		if user == parola:
			print(f'access granted\n')
			return True
		print('Password wrong!')
		tries += 1

	print('--> Too many tries!')
	return False

#---------------------
# Main Program
#---------------------

def main():

	if not get_pass():
		return

	phone = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

	adri = {}


	for line in phone:
		word = line.decode().strip().split()

		if len(word) < 4:
			continue

		ceva = word[3]
		adri[ceva] = adri.get(ceva, 0) + 1



	for key, value in adri.items():
		print(key, value)



	#------------------------------
	# Save the result in result.txt
	#------------------------------

	with open('result.txt', 'w') as f:
		f.write('word counting\n')
		f.write('--------------\n\n')
		for key, value in adri.items():
			f.write(f'{key}: {value}\n')

	print('Created result.txt file')


main()


