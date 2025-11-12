''' Extracting Data'''

import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()

	if re.search('ˆFrom:', line):
		print(line)

#-----------------

''' Matching and Extracting Data using re.findall() '''

# ex:

import re 
x = 'My favorite 2 numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)

#----------------
# ex:

import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x) # starting with F, (.+)-any caracter, (?)-don't be greedy(not greedy prefer the shortest)
y = re.findall('^F.+:', x) # starting with F, (.+) any caracter and be greedy(be greedy prefer the longest)
print(y)

#--------------------------------------

# ex:

import re
file = input('insert file name:')
if len(file) < 3:
	file = 'mbox-short.txt'

filename = open(file)

for y in filename:
	if not y.startswith('From '):
		continue
	y = y.strip()
	# print(y)
	y = re.findall(r'^From (\S+@\S+)', y) # The r tells Python: “Treat this string literally — don’t interpret \S as an escape sequence.”
	print(y)

#-------------------------------------

''' The Double Split Pattern --> The Regex Version '''

# ex:
import re

file = input('insert file name:')
if len(file) < 3:
	file = 'mbox-short.txt'


filename = open(file)



for line in filename:
	if not line.startswith('From '):
		continue

	line = line.rstrip()
	
	# print(line)

	word = re.findall(r'@([^ ]*)', line)
	print(word)

















