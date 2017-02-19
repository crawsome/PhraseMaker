import random
import re
import sys
import os

# randomly selects 4 words. Sometimes, they are funny. 
# Save words with 1, blacklist them with 2, exit with 0. 
# all files are written to text files. 

# Places 2 words from the beginning and end, 
# and 2 from a dictionary which I got here:
# https://github.com/dwyl/english-words
# 2016 Colin Burke

def main():
	# program reads in blacklist, whitelist, and dictionary
	stuff = open('words2.txt', 'r')
	goodlist = open('good.txt', 'r')
	badlist = open('bad.txt', 'r')
	
	# comes before the two words
	prefix = ['Check out the ', 'A ', 'One ', 'Two ', 'Three ',
	'Dealing with ', 'It\'s time for ', 'Who else but ', 
	'Do we really need another ', 'There was a ', 'Beware of ', 
	'The ', 'The ', 'An evening with ', 'Fuck ', 
	'Good times with ', 'Did you hear about the ', 
	'I once ate an entire ',]
	
	# comes after the two words
	addendum = ['industries', 'inc.', 'limited', 'club band', 
	'handbook', 'esq.', '!', '!', '!', '!', '!', '!', '?', '?', 
	'?', '?', '', '', '', '', '', '', '']
	
	# retrieve dictionary
	data = []
	for word in stuff:
		data.append(word)
	
	# retrieve blacklist
	markedbad = []
	for word in badlist:
		markedbad.append(word)
	badlist.close()
	badlist = open('bad.txt', 'w')
	
	# retrieve whitelist (for additions)
	markedgood = []
	for word in goodlist:
		markedgood.append(word)
	goodlist.close()
	goodlist = open('good.txt', 'w')
	
	# loop condition
	going = 1
	
	size = len(data)
	lasttry = 'qwerpoiuqwerpoi'
	
	while going > 0:
	
		# random ranges
		datarand1 = random.randint(0, size)
		datarand2 = random.randint(0, size)
		prefixrand = random.randint(0,len(prefix)-1)
		addrand = random.randint(0, len(addendum)-1)
		
		# make our proposed string, and make sure it doesn't exist in the blacklist
		lasttry = str(prefix[prefixrand] + data[datarand1] + ' ' + data[datarand2] + ' ' + addendum[addrand])
		lasttry = re.sub('\n','', lasttry)
		
		while lasttry in markedbad:
			lasttry = str(prefix[prefixrand] + data[datarand1] + ' ' + data[datarand2] + ' ' + addendum[addrand])
			lasttry = re.sub('\n','', lasttry)
		print lasttry
		
		going = input('0 to exit, 1 to keep, 2 to trash')
		
		print going
		
		if going == 0:
			print 'exiting'
		elif going == 1:
			print 'saving'
			markedgood.append(lasttry)
		elif going == 2:
			print 'excluding'
			markedbad.append(lasttry)
			
		
	for good in markedgood:
		goodlist.write(good + '\n')
	goodlist.close()
	
	for bad in markedbad:
		badlist.write(bad+ '\n')
	badlist.close()
	
	return
	
main()
