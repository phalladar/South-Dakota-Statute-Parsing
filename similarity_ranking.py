import difflib

def compareText(ddisk, website):
	seq = difflib.SequenceMatcher(None, ddisk, website)
	return seq.ratio() * 100

def findDifferences(ddisk, website):
	#d = difflib.Differ()
	diff = difflib.unified_diff(ddisk.splitlines(), website.splitlines(), lineterm='')
	return '\n'.join(list(diff))


a = '34A-3A-6. Exemption of public water supply systems--Requirements. The secretary may exempt any public water supply system from any maximum contaminant level upon finding that:\n(1) Due to compelling factors, including economic, the public water system is unable to comply with the contaminant level. In assessing the compelling factors the secretary shall consider such factors as construction, installation, or modification of treatment equipment or systems, and the time needed to replace an existing noncomplying facility with a new treatment system;\n(2) The public water system was in operation on the effective date of the maximum contaminant level regulations;\n(3) The granting of the exemption will not result in an unreasonable risk to health; and\n(4) Within one year of the date of exemption authorization, a schedule for compliance be issued and the owner of the supply agree to implement the schedule.\nSource:\n  SL 1983, ch 260, \xa7 6.'
b = '34A-3A-6. Exemption of public water supply systems--Requirements. The secretary may exempt any public water supply system from any maximum contaminant level upon finding that:\n (1) Due to compelling factors, including economic, the public water system is unable to comply with the contaminant level. In assessing the compelling factors the secretary shall consider such factors as construction, installation, or modification of treatment equipment or systems, and the time needed to replace an existing noncomplying facility with a new treatment system;\n (2) The public water system was in operation on the effective date of the maximum contaminant level regulations;\n (3) The granting of the exemption will not result in an unreasonable risk to health; and\n (4) Within one year of the date of exemption authorization, a schedule for compliance be issued and the owner of the supply agree to implement the schedule.\n \n Source: SL 1983, ch 260, &#167; 6. \n '
c = ' 35-4-2.10. Repealed by SL 2009, ch 177, \xa7 8.\n'
d = ' 35-4-2.10. Repealed by SL 2009, ch 177, &#167; 8.\n '

print compareText(a, b)
print compareText(c, d)
print findDifferences(c, b).decode('utf-8', 'ignore')