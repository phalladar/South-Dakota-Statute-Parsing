import difflib, pickle, HTMLParser

def compareText(ddisk, website):
	seq = difflib.SequenceMatcher(None, ddisk, website)
	return seq.ratio() * 100

def findDifferences(ddisk, website):
	#d = difflib.Differ()
	diff = difflib.unified_diff(ddisk.splitlines(), website.splitlines(), lineterm='')
	return '\n'.join(list(diff))

bigDict = {}

a = '34A-3A-6. Exemption of public water supply systems--Requirements. The secretary may exempt any public water supply system from any maximum contaminant level upon finding that:\n(1) Due to compelling factors, including economic, the public water system is unable to comply with the contaminant level. In assessing the compelling factors the secretary shall consider such factors as construction, installation, or modification of treatment equipment or systems, and the time needed to replace an existing noncomplying facility with a new treatment system;\n(2) The public water system was in operation on the effective date of the maximum contaminant level regulations;\n(3) The granting of the exemption will not result in an unreasonable risk to health; and\n(4) Within one year of the date of exemption authorization, a schedule for compliance be issued and the owner of the supply agree to implement the schedule.\nSource:\n  SL 1983, ch 260, \xa7 6.'
b = '34A-3A-6. Exemption of public water supply systems--Requirements. The secretary may exempt any public water supply system from any maximum contaminant level upon finding that:\n (1) Due to compelling factors, including economic, the public water system is unable to comply with the contaminant level. In assessing the compelling factors the secretary shall consider such factors as construction, installation, or modification of treatment equipment or systems, and the time needed to replace an existing noncomplying facility with a new treatment system;\n (2) The public water system was in operation on the effective date of the maximum contaminant level regulations;\n (3) The granting of the exemption will not result in an unreasonable risk to health; and\n (4) Within one year of the date of exemption authorization, a schedule for compliance be issued and the owner of the supply agree to implement the schedule.\n \n Source: SL 1983, ch 260, &#167; 6. \n '
c = ' 35-4-2.10. Repealed by SL 2009, ch 177, \xa7 8.\n'
d = ' 35-4-2.10. Repealed by SL 2009, ch 177, &#167; 8.\n '

statutetoCompare = '34A-3A-6'

web = pickle.load(open("web_complete.p"))
ddisk = pickle.load(open("ddisk2.p"))

# print ddisk[statutetoCompare]['ddisk_text']
# print web[statutetoCompare]['web_text']

# print str(compareText(ddisk[statutetoCompare]['ddisk_text'], web[statutetoCompare]['web_text'])) + " match on text"
# print str(compareText(ddisk[statutetoCompare]['ddisk_title'], web[statutetoCompare]['title'])) + " match on title"

for i in web:
	#print i, web[i]['title']
	try:
		if web[i]['title'].find('...') != -1:
			theDDiskTitle = ddisk[i]['ddisk_title'][:web[i]['title'].find('...')] + '...'
		else:
			theDDiskTitle = ddisk[i]['ddisk_title']

		htmlConvert = HTMLParser.HTMLParser() # convert HTML reminants

		bigDict[i] = { 'web_text': htmlConvert.unescape(web[i]['web_text']),
					   'web_title': htmlConvert.unescape(web[i]['title']),
					   'url': web[i]['url'],
					   'ddisk_text': ddisk[i]['ddisk_text'],
					   'ddisk_title': theDDiskTitle,
					   'text_similar': None,
					   'title_similar': None }
	except Exception:
		if len(i.split("-")) > 2:
			print "Problem in key " + i

for j in bigDict:
	try:
	 	bigDict[j]['text_similar'] = compareText(bigDict[j]['web_text'], bigDict[j]['ddisk_text'])
	 	bigDict[j]['title_similar'] = compareText(bigDict[j]['web_title'], bigDict[j]['ddisk_title'])
	except Exception:
		print 'Compare error in ' + str(j)


print bigDict['36-21A-59']

pickle.dump( bigDict, open("similar_dict.p", "wb"))