 # coding=utf-8
import re, pprint, pickle, codecs
import difflib, pickle, HTMLParser

def compareText(ddisk, website):
	seq = difflib.SequenceMatcher(lambda x: x in "Â", ddisk, website)
	return seq.ratio() * 100

def findDifferences(ddisk, website):
	text1 = ddisk.splitlines()
	text2 = website.splitlines()
	d = difflib.Differ()
	diff = d.compare(text1, text2)
	return '\n'.join(diff)


theBigDict = pickle.load(open("similar-dict-34a-43-NEW.p"))

statute = '37-25A-47'

ddisk = theBigDict[statute]['ddisk_text']
web = theBigDict[statute]['web_text']

#print(findDifferences(web, ddisk)).decode('utf-8', 'ignore')
print ddisk.decode('utf-8', 'ignore')
print web.decode('utf-8', 'ignore')

