''' Spam Confidence '''

import re

file = input('insert file name:')
if len(file) < 3:
	file = 'mbox-short.txt'

filename = open(file)


for line in filename:
	line = line.rstrip()
	word = re.findall(r'^X-DSPAM-Confidence: ([0-9.]*?)', line)
	if len(word) != 1:
		continue

	num = float(word[0])
	numlist.append(num)
	print(numlist)
	