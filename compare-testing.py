 # coding=utf-8
import re, pprint, pickle, codecs
import difflib, pickle, HTMLParser

def compareText(ddisk, website):
	seq = difflib.SequenceMatcher(lambda x: x in "Â", ddisk, website)
	return seq.ratio() * 100

def findDifferences(ddisk, website):
	#d = difflib.Differ()
	diff = difflib.unified_diff(ddisk.splitlines(), website.splitlines(), lineterm='')
	return '\n'.join(list(diff))

test1 = """43-8-4. Recovery of rent dependent upon life of another. Rent dependent upon the life of a person may be recovered after as well as before his death.  Source: CivC 1877, Â§ 263; CL 1887, Â§ 2779; RCivC 1903, Â§ 286; RC 1919, Â§ 356; SDC 1939, Â§ 51.0708.  """.strip()
test2 = """43-8-4. Recovery of rent dependent upon life of another. Rent dependent upon the life of a person may be recovered after as well as before his death.Source:  CivC 1877, § 263; CL 1887, § 2779; RCivC 1903, § 286; RC 1919, § 356; SDC 1939, § 51.0708.          Source:""".strip()

print compareText(test1, test2)



