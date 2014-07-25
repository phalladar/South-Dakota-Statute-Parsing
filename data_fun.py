# coding=utf-8
from __future__ import print_function
import re, pprint, pickle, codecs
import difflib, pickle, HTMLParser


def compareText(ddisk, website):
	seq = difflib.SequenceMatcher(None, ddisk, website)
	return seq.ratio() * 100

def findDifferences(ddisk, website):
	text1 = ddisk.splitlines()
	text2 = website.splitlines()
	return '\n'.join(list(diff))

theBigDict = pickle.load(open("similar-dict-34a-43-NEW.p"))

f = open("text-match.txt", "w")
byeReturns = re.compile(r'[\n|\r|\t]')



print('Statute' + '\t' + 'Text Similar' + '\t' + 'Title Similar' + '\t' + 'Web Text NEW' + '\t' + 'Dakota Disk Text' + '\n', file=f)
for i in theBigDict:
	print(str(i) + '\t' + str(theBigDict[i]['text_similar']) + '\t' + str(theBigDict[i]['title_similar']) + '\t' + re.sub(byeReturns, '', str(theBigDict[i]['web_text'])) + '\t' + re.sub(byeReturns, '', str(theBigDict[i]['ddisk_text'])), file=f)

# statute = '35-4-97'

# print theBigDict[statute]['web_text']
# print chardet(theBigDict[statute]['ddisk_text'])
f.close()