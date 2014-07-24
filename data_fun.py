# coding=utf-8
from __future__ import print_function
import re, pprint, pickle, codecs
import difflib, pickle, HTMLParser

def compareText(ddisk, website):
	seq = difflib.SequenceMatcher(None, ddisk, website)
	return seq.ratio() * 100

def findDifferences(ddisk, website):
	#d = difflib.Differ()
	diff = difflib.unified_diff(ddisk.splitlines(), website.splitlines(), lineterm='')
	return '\n'.join(list(diff))

theBigDict = pickle.load(open("similar-dict-34a-43.p"))

f = open("text-match.txt", "w")
byeReturns = re.compile(r'[\n|\r|\t]')

print('Statute' + '\t' + 'Text Similar' + '\t' + 'Title Similar' + '\t' + 'Web Text' + '\t' + 'Dakota Disk Text' + '\n', file=f)
for i in theBigDict:
	print(str(i) + '\t' + str(theBigDict[i]['text_similar']) + '\t' + str(theBigDict[i]['title_similar']) + '\t' + re.sub(byeReturns, '', str(theBigDict[i]['web_text'])) + '\t' + re.sub(byeReturns, '', str(theBigDict[i]['ddisk_text'])), file=f)

# statute = '36-20B-1'

# print theBigDict[statute]['web_text']
# print chardet(theBigDict[statute]['ddisk_text'])
f.close()