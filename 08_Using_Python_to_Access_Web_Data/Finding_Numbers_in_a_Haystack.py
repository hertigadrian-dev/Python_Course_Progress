# Finding_Numbers_in_a_Haystack.py
# Author: Hertig Adrian
# Description: Reads 'regex_sum_2311578.txt' / 'regex_sum_42.txt', Reads a text file, extracts all numbers 
# using re.findall(r'\d+'), converts them to integers, and computes the total sum.
# Source: Using Python to Access Web Data (Chapter 11)
# Date: 2025-11-16



''' In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

Data Files
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_2311578.txt (There are 112 values and the sum ends with 871)
These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.
Data Format
The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. Here is a sample of the output you might see:

Why should you learn to write programs? 7746
12 1929 8827
Writing programs (or programming) is a very creative 
7 and rewarding activity.  You can write programs for 
many reasons, ranging from making your living to solving
8837 a difficult data analysis problem to having fun to helping 128
someone else solve a problem.  This book assumes that 
everyone needs to know how to program ...
The sum for the sample text above is 27486. The numbers can appear anywhere in the line. There can be any number of numbers in each line (including none).
Handling The Data
The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

  '''	

#---------------------------------------
#For file: 'regex_sum_42.txt' we have:


import re 

file = input('insert file name:')
if len(file) < 3:
	file = 'regex_sum_42.txt'
filename = open(file)

adri = list()

total = 0

for line in filename:
  	line = line.rstrip()
  	extr = re.findall(r'\d+', line)
  	for num in extr:
  		total += int(num)

print(total)

#----------------------------------------
# For file name: 'regex_sum_2311578.txt' we have:


import re

file = input('file name:')
if len(file) < 3:
	file = 'regex_sum_2311578.txt'

filename = open(file)

total = 0

for line in filename:
	line = line.rstrip()
	extr = re.findall(r'\d+', line)
	# print (extr)
	for num in extr:
		total = total + int(num)
print(total)







