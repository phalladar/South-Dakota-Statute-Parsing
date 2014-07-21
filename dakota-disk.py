# coding=utf-8
import re, pprint, pickle

theString = open("sdcode-full.txt", "r").read()

theString = re.sub(r'\d*[A-Z]?-\d*[A-Z]?-\d*[\.\d]*[A-Z]?[-\d*[\.\d]*[A-Z]?]?[\w\(\)]*\s.*\(\d*[A-Z]?-\d*[A-Z]?-\d*[\.\d]*[A-Z]?[-\d*[\.\d]*[A-Z]?]?[\w\(\)]*.*(?:and|to|\,).*\)', "", theString)
# remove stupid things like 15-6-4 PROCESS. (15-6-4(a) to 15-6-4(j))

ddisk_dict = {}
tempArray = []


theTitles = re.findall(r"\n(\d*[A-Z]?-\d*[A-Z]?-\d*[\.\d]*[A-Z]?[-\d*[\.\d]*[A-Z]?]?[\w\(\)]*)(?:\t|\sto|\,)?.*\t(.*\.?)", theString, re.MULTILINE) # find statute titles from headings
for k in theTitles:
	ddisk_dict[k[0]] = { 'ddisk_title': k[1],
						  'ddisk_text': None }
	#print k[0]

theString = re.sub(r'\n\d*[A-Z]?-\d*[A-Z]?-\d*[\.\d]*[A-Z]?[-\d*[\.\d]*[A-Z]?]?[\w\(\)]*(?:\t|\sto|\,)?.*\t.*\.', "", theString, re.MULTILINE) # dispose of the headings

grabStatutes = re.findall(r'^(\d+[\w+]?-(?:\d+[\w+]?-\d+[\w+]?-\d+[\w+]?)?(?:[,.\-0-9A-Z\(\)\w]+)?[ \t]+.*?(?=\n\n|\n+\Z|\Z))', theString, re.MULTILINE | re.DOTALL) # get the text of all the statutes

for i in grabStatutes:
	try:
		theSection = re.findall(r'(\d+\w?-\d+[-0-9A-Z\.]*)(?:\s|\,)', i)
		theRealSection = theSection[0]
		theText = re.sub(r'\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*.*\n\t +', "", i)
		ddisk_dict[theRealSection]['ddisk_text'] = theText
		#print theSection[0]
	except Exception:
		theSection = re.findall(r'(\d*[A-Z]?-\d*[A-Z]?-\d*[\.\d]*[A-Z]?[-\d*[\.\d]*[A-Z]?]?[\w\(\)]*)(?:\t|\sto|\,)?', i)
		theRealSection = theSection[0]
		print theRealSection
		
# Use the below to test specific statutes
#print ddisk_dict['36-21A-59']

# Use the below to pickle dump the entire database
pickle.dump( ddisk_dict, open("ddisk2.p", "wb"))