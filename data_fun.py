# coding=utf-8
import re, pprint, pickle
import difflib, pickle, HTMLParser

def compareText(ddisk, website):
	seq = difflib.SequenceMatcher(None, ddisk, website)
	return seq.ratio() * 100

def findDifferences(ddisk, website):
	#d = difflib.Differ()
	diff = difflib.unified_diff(ddisk.splitlines(), website.splitlines(), lineterm='')
	return '\n'.join(list(diff))

theBigDict = pickle.load(open("similar-dict-1-34.p"))

# for i in theBigDict:
# 	print str(i) + '\t' + str(theBigDict[i]['text_similar']) + '\t' + str(theBigDict[i]['title_similar'])

statute = '13-21-1'

print theBigDict[statute]