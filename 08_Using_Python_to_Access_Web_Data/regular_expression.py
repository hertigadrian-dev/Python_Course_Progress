''' Spam Confidence using regex'''

# import re

# file = input('insert file name:')
# if len(file) < 3:
# 	file = 'mbox-short.txt'

# filename = open(file)

# numlist = list()

# for line in filename:
# 	line = line.rstrip()
# 	word = re.findall(r'^X-DSPAM-Confidence: ([0-9.]*)', line)
# 	# print(word)
# 	if len(word) != 1:
# 		continue
# 	print(word)

# 	num = float(word[0])
# 	numlist.append(num)
# print(max(numlist))
# print('Maximum:', max(numlist))
	

import re

file = input('insert file name:')
if len(file) < 3:
	file = 'mbox-short.txt'

filename = open(file)

adri = list()

for line in filename:
	line = line.rstrip()

	extract = re.findall(r'^X-DSPAM-Confidence: ([0-9.]+)', line)
	if len(extract) != 1:
		continue
	# print(extract)
	num = float(extract[0])
	
	adri.append(num)
print(max(adri))

