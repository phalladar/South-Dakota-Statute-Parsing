# coding=utf-8
import re, pprint, pickle

theString = open(r"C:\sdcode.txt", "r").read()

ddisk_dict = {}
tempArray = []

theTitles = re.findall(r"\n(\d+\w?-\d+[-0-9A-Z\.]*)[,| to|\t](.*)(?!\.\n)", theString) # find statute titles from headings
for k in theTitles:
	ddisk_dict[k[0]] = { 'ddisk_title': k[1],
						  'ddisk_text': None }

theString = re.sub(r'\n\d+\w?-\d+[-0-9A-Z\.]*[,| to|\t].*(?!\.\n)', "", theString) # dispose of the headings

#print theString.decode('utf-8', 'ignore')

grabStatutes = re.findall(r'^(?:\t |\n)(\d+[\w+]?-(?:\d+[\w+]?-\d+[\w+]?-\d+[\w+]?)?(?:[,.\-0-9A-Z]+)?[ \t]+.*?(?=\n\n|\n+\Z|\Z))', theString, re.MULTILINE | re.DOTALL) # get the text of all the statutes

for i in grabStatutes:
	theSection = re.findall(r'(\d+\w?-\d+[-0-9A-Z\.]*)[\.| to|,](?:\s|\,|to)', i)
	theRealSection = theSection[0]
	theText = re.sub(r'\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*.*\n\t +', "", i)
	ddisk_dict[theRealSection]['ddisk_text'] = theText
	#print theSection[0]


# Use the below to test specific statutes
print ddisk_dict['36-21A-59']

# Use the below to pickle dump the entire database
pickle.dump( ddisk_dict, open("ddisk2.p", "wb"))