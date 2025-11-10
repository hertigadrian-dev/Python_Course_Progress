# cabinet = dict()

# cabinet ['summer'] = 12
# cabinet ['fall'] = 3
# cabinet ['spring'] = 75

# print (cabinet)

# print(cabinet['fall'])

# cabinet ['fall'] = cabinet['fall'] + 2
# print (cabinet)
# #--------------------

# lst = list()

# lst.append(21)
# lst.append(182)
# print(lst)

# lst[0] = 23
# print(lst)


# lsc = dict()

# lsc['age'] = 21
# lsc['course'] = 128
# print(lsc)

# lsc['age'] = 23
# print(lsc)
#---------------------

# ex of Counting:

# countt = dict()
# countt['csev'] = 1
# countt['cwen'] = 1
# print(countt)

# countt['csev'] = countt['csev'] + 1
# print (countt)

# print('csev' in countt)

#------------------------

# countt = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

# for x in names:
# 	if x not in countt:
# 		countt[x] = 1
# 	else:
# 		countt[x] = countt[x] + 1
# countt['apple'] = countt.get('apple',0) + 1
# print(countt) 

#---------------------

# alt exemplu de .get() - automatic counting:

# for x in names:
# 	countt[x]= countt.get(x, 0) + 1
# print(countt)


# ab = dict()
# frutas = ['apple', 'greps','orange','cherry']

# for x in frutas:
# 	# ab[x] = ab.get(x, 0) +1
# 	if x not in ab:
# 		ab[x] = 1
# 	else:
# 		ab[x] = ab[x] + 1
# ab['plato'] = ab.get('plato', 0) + 1
# print(ab)
 
#------------------
'''9.4 Write a program to read through the mbox-short.txt and figure out who 
has sent the greatest number of mail messages. The program looks for 'From ' lines 
and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address 
to a count of the number of times they appear in the file. After the dictionary 
is produced, the program reads through the dictionary using a maximum loop to find 
the most prolific committer. '''


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

ab = dict()

for line in handle:
	line = line.rstrip()
	if not line.startswith('From '): continue

	words = line.split()
	email = words[1]
	ab[email] = ab.get(email, 0) + 1
# print(ab)

count_email = None
nr_count = 0

for email, count in ab.items():
	if count>nr_count:
		nr_count = count 
		count_email = email 
print(count_email, nr_count)





	

























