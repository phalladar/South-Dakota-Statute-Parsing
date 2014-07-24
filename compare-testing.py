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


# test1 = """43-8-4. Recovery of rent dependent upon life of another. Rent dependent upon the life of a person may be recovered after as well as before his death.  Source: CivC 1877, Â§ 263; CL 1887, Â§ 2779; RCivC 1903, Â§ 286; RC 1919, Â§ 356; SDC 1939, Â§ 51.0708.  """.strip()
# test2 = """43-8-4. Recovery of rent dependent upon life of another. Rent dependent upon the life of a person may be recovered after as well as before his death.Source:  CivC 1877, § 263; CL 1887, § 2779; RCivC 1903, § 286; RC 1919, § 356; SDC 1939, § 51.0708.          Source:""".strip()
# test1 = """ 37-5-1.1. Omitted """
# test2 = """37-5-1.1. Omitted"""
# test1 = """ 35-4-2.1. Local approval of Sunday sales by on-sale licensees. Notwithstanding Â§ 35-4-81 , the governing body of any municipality or county may, in its discretion, provide in any on-sale license the right to sell, serve, or allow to be consumed alcoholic beverages on Sunday except between the hours of two a.m. and seven a.m.  Source: SL 1973, ch 237, Â§ 2; SL 1974, ch 247; SL 1975, ch 229; SL 1990, ch 297; SL 2003, ch 192, Â§ 1; SL 2009, ch 173, Â§ 1.  """
# test2 = """35-4-2.1. Local approval of Sunday sales by on-sale licensees. Notwithstanding § 35-4-81, the governing body of any municipality or county may, in its discretion, provide in any on-sale license the right to sell, serve, or allow to be consumed alcoholic beverages on Sunday except between the hours of two a.m. and seven a.m.Source:  SL 1973, ch 237, § 2; SL 1974, ch 247; SL 1975, ch 229; SL 1990, ch 297; SL 2003, ch 192, § 1; SL 2009, ch 173, § 1.          Source:"""
test1 = """37-33-11. Burden of proof. The burden of showing compliance with the provisions of Â§Â§ 37-33-1 to 37-33-11 , inclusive, lies with the plan, scheme, or person involved with such plan or scheme.  Source: SL 2003, ch 213, Â§ 11.  """
test2 = """37-33-11. Burden of proof. The burden of showing compliance with the provisions of §§ 37-33-1 to 37-33-11, inclusive, lies with the plan, scheme, or person involved with such plan or scheme.Source:  SL 2003, ch 213, § 11.          Source:"""


test1 = re.sub(r'Â', "", test1).strip()
test2 = re.sub(r'\s\s\s\s*Source\:', "", test2).strip()
test2 = re.sub(r'\.Source', r'.  Source', test2)
print test1
print test2
print compareText(test1, test2)



