# ex9_4_max_email_sender.py
# Author: Hertig Adrian
# Description: Reads mbox-short.txt, extracts email addresses from 'From ' lines,
# and finds which address appears most often.
# Source: Python for Everybody (Chapter 9)
# Date: 2025-11-11



'''9.4 Write a program to read through the mbox-short.txt and figure out who 
has sent the greatest number of mail messages. The program looks for 'From ' lines 
and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address 
to a count of the number of times they appear in the file. After the dictionary 
is produced, the program reads through the dictionary using a maximum loop to find 
the most prolific committer. '''



# name = input('insert file name:')

# if len(name) < 1:
# 	name = 'mbox-short.txt'

# filename = open(name)

# adi = dict()

# for line in filename:
# 	line = line.rstrip()

# 	if not line.startswith('From'):
# 		continue

# 	word = line.split()
# 	# print (word)

# 	extr = f'{word[1]}'
# 	# print(extr)

# 	adi[extr]=adi.get(extr, 0) + 1
# 	# print(adi)

# nr_email=None

# nr_email = max(adi, key=adi.get)
# print(nr_email, adi[nr_email])
#------------------------------------------------

# Actually the same thing:

file = input('insert file name:')
if len(file) < 2:
	file = 'mbox-short.txt'

filename = open(file)
# print (filename)

adri = {} # I create an empty dictionary

for line in filename: # starts a loop that reads the file line by line. Each time trough the loop the variable 'line' holds one line from the file.
	if not line.startswith('From'): #check if the curent line begins with word "From"  
		continue # # If the line doesn’t start with "From", we skip it and go back to the top of the loop for the next line.

	line = line.rstrip() # eliminate empty space , removes newlines (\n) at the end of the line
	line = line.split() # Splits the line into a list of words, separated by spaces.
	# print(line)
	word = f'{line[1]}' #Takes the second word in the line (line[1]) — that’s the email address. Stores it in a variable called word.
	# print(word)

	adri[word] = adri.get(word, 0) + 1 # it does automatic counting using a dictionary. adri.get(word, 0) → gets the current count of that email (or 0 if it’s not in the dictionary yet).
	# print(adri)

nr_email = max(adri, key=adri.get) # Finds the key (email) with the highest value (count).

''' adri.get gives the “value” (count)
max(..., key=adri.get) finds which key has the largest count. '''

print(nr_email, adri[nr_email])





#-----------------------------------------

''' Playing around: '''

# adi = ['The apple is green','The cherries are reds', 'The melon is yellow', 'The apple is green', 'peach','cherry','orange juce for clients', 'apple']
# anc = ['red is a color','blue is my car ', 'red color is my flag']
# tot = adi + anc

# blue = {}
# for line in tot:
# 	blue[line] = blue.get(line, 0) + 1
# 	# print(blue)
# for key, value in sorted(blue.items(), reverse=True):
# 	print(value, key)

#---------------------------------------	

# blue = {'apple': 2, 'banana': 1, 'cherry': 3}
# w = list(blue.items())
# print(w[0][0])

# my_list = ['apple', 2, 'banana', 1, 'cherry', 3]

# blue = {}

# for line in my_list:
# 	blue[line] = blue.get(line, 0) + 1
# 	print(blue)









	






