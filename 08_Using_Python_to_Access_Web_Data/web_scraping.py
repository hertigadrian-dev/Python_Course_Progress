# -----------------------------------------------
# File: web_craping.py
# Author: Hertig Adrian
# Description: Using Python to Access Web Data
# Source: Programs that Surf the Web (Chapter 12)
# Date: 2025-11-22


# Web scraping = programmatically collecting information from websites / extracting meaningful information.
''' We scrape because websites contain valuable information, and scraping 
lets us extract it automatically for analysis, automation, or building applications.'''

#--------------------------

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

# import ssl

# # ignore SSL certificate errors
# ctx = ssl._create_unverified_context()


# url = input('enter url: ')
# try:
# 	html = urllib.request.urlopen(url, context=ctx).read()
# except:
# 	print('invalid url or connection problem!')
# 	quit()

# soup = BeautifulSoup(html, 'html.parser')

# # retrive all the anchor tags

# tags = soup.find_all('a')

# for ceva in tags:
# 	word = (ceva.get('href', None))
# 	if not word.startswith('https'):
# 		continue

# 	word1 = word.split('//')[1]
	
# 	print(word1)

#-----------------------------


import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

ctx = ssl._create_unverified_context()

url = input('insert url: ') or 'http://www.dr-chuck.com'



try:
	html = urllib.request.urlopen(url, context=ctx).read()
except:
	print('invalid url')
	quit()


soup = BeautifulSoup(html, 'html.parser')

tag = soup.find_all('a')

for ceva in tag:
	word = ceva.get('href')
	if word is None:
		continue
	if word.startswith('#'):
		continue
	if word.startswith('javascript:'):
		continue
	if word.startswith('mailto:'):
		continue
	# print(word)
	if word.startswith('/'):
		word = url + word

	if not word.startswith('http'):
		continue

	word1 = word.strip()
	word2 = word1.split('/')

	word2 = [x for x in word2 if x][1]
	
	print(word2) 







	



























# ex.1
# import requests
# url = 'http://data.pr4e.org'
# response = requests.get(url)
# html = response.text

# print("----- HTML CONTENT -----\n")
# print(html)


# ex.2

# import requests
# from bs4 import BeautifulSoup

# url = 'http://data.pr4e.org'
# response = requests.get(url)

# soup = BeautifulSoup(response.text, 'html.parser')

# links = soup.find_all('a')

# for link in links:
#     print(link.get('href'))

#--------------------------

# import requests
# from bs4 import BeautifulSoup

# url = 'http://data.pr4e.org'
# response = requests.get(url)
# html = response.text

# soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify()) 