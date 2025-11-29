x =list()
x+=['para','mar'] # the same as: x.extend(['para', 'mar']) 
print(x)

#------------------------------------
#ex: eliminate whitespace/(index[1]):
#------------------------------------

word2 = ['https:', '', 'www.youtube.com', 'watch?v=BVKpW02hsrU']


adri_list = []

for x in word2:
	if x:
		adri_list.append(x)
word2 = adri_list
print(word2)

#-------------------------------------------
''' the same thing as above in one line: '''
#-------------------------------------------

word2 = [x for x in word2 if x]
print(word2)

