
# import re
# hand = open('mbox-short.txt')
# for line in hand:
# 	line = line.rstrip()

# 	if re.search('ˆFrom:', line):
# 		print(line)


import re 
x = 'My favorite 2 numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
