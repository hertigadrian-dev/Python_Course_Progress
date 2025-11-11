# exercise_10_2_hour_distribution.py
# Author: Hertig Adrian
# Description: Reads mbox-short.txt and counts the distribution of messages by hour.
# Source: Python Data Structures (Chapter 10)
# Date: 2025-11-11





''' 10.2 Write a program to read through the mbox-short.txt and 
figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and 
then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, 
sorted by hour as shown below.  '''


file = input('insert file name:')
if len(file) < 3:
	file = 'mbox-short.txt'

filename = open(file)

adri = {}

for line in filename:
	if not line.startswith('From '):
		continue

	line = line.strip()
	line = line.split()
	
	hour = line[5].split(':')[0]
	# first = hour.split(':')
	# second = first[0]
	# print(second)

	adri[hour] = adri.get(hour, 0) + 1
	# print(adri)
handle = list(adri.items())
# print(handle)

for key, value in adri.items():
	print(key, value)
