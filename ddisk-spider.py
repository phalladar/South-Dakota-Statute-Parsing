# coding=utf-8

import re, urllib, htmlentitydefs

def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)

def isAlphaNumInRange(theSection, theMin, theMax):
	# This code is necessary to rank numbers against
	# alphanumerals for ordering purposes

	sectionRegEx = re.findall(r'(\d+)(\w)?', theSection)
	for i in sectionRegEx:
		if i[1]: # if there's a letter appended at the end of the section evaluate it
			theValue = float(i[0]) + convertAlpha(i[1])
		else:
			theValue = float(i[0])

	minRegEx = re.findall(r'(\d+)(\w)?', theMin)
	for j in minRegEx:
		if j[1]:
			theMin = float(j[0]) + convertAlpha(j[1])
		else:
			theMin = float(j[0])

	maxRegEx = re.findall(r'(\d+)(\w)?', theMax)
	for k in maxRegEx:
		if k[1]:
			theMax = float(k[0]) + convertAlpha(k[1])
		else:
			theMax = float(k[0])

	if theValue >= theMin and theValue <= theMax:
		return True
	else:
		return False

def convertAlpha(alpha):
	if alpha == 'A':
		return 1.0 / 27
	if alpha == 'B':
		return 1.0 / 26
	if alpha == 'C':
		return 1.0 / 25
	if alpha == 'D':
		return 1.0 / 24
	if alpha == 'E':
		return 1.0 / 23
	if alpha == 'F':
		return 1.0 / 22
	if alpha == 'G':
		return 1.0 / 21
	if alpha == 'H':
		return 1.0 / 20
	if alpha == 'I':
		return 1.0 / 19
	if alpha == 'J':
		return 1.0 / 18
	if alpha == 'K':
		return 1.0 / 17
	if alpha == 'L':
		return 1.0 / 16
	if alpha == 'M':
		return 1.0 / 15
	if alpha == 'N':
		return 1.0 / 14
	if alpha == 'O':
		return 1.0 / 13
	if alpha == 'P':
		return 1.0 / 12
	if alpha == 'Q':
		return 1.0 / 11
	if alpha == 'R':
		return 1.0 / 10
	if alpha == 'S':
		return 1.0 / 9
	if alpha == 'T':
		return 1.0 / 8
	if alpha == 'U':
		return 1.0 / 7
	if alpha == 'V':
		return 1.0 / 6
	if alpha == 'W':
		return 1.0 / 5
	if alpha == 'X':
		return 1.0 / 4
	if alpha == 'Y':
		return 1.0 / 3
	if alpha == 'Z':
		return 1.0 / 2
	return 0 # if there's no alpha associated return 0

def startCrawling(website):
	if website != '/':
		for statuteURL in re.findall('''<A HREF="(/Statutes/Codified_Laws.*Statute=.*)">''', urllib.urlopen(website).read(), re.I):
			statuteURL = 'http://legis.sd.gov' + statuteURL
			if statuteURL not in activeStatutes and statuteURL not in visitedStatutes and statuteURL != '/':
			 	activeStatutes.append(statuteURL)
	if website not in visitedStatutes: visitedStatutes.append(website)
	activeStatutes.remove(website)

theOldURL = 'http://legis.sd.gov/Statutes/Codified_Laws/default.aspx'

theMin = '34A'
theMax = '43'

activeStatutes = []
visitedStatutes = []

for theNewURL in re.findall('''td\>\<a\shref=\"\/Statutes(.*[^ ]\=(\d*\w*))''', urllib.urlopen(theOldURL).read(), re.I):
	if isAlphaNumInRange(theNewURL[1], theMin, theMax):
		activeStatutes.append('http://legis.sd.gov/Statutes' + unescape(theNewURL[0]))

while activeStatutes:
	if len(activeStatutes[0].split('-')) < 3:
		startCrawling(activeStatutes[0])
	else:
 		#getStatuteContent(activeStatutes[0])
		if activeStatutes[0] not in visitedStatutes: visitedStatutes.append(activeStatutes[0])
	print "Finished processing: " + activeStatutes[0]
	activeStatutes.remove(activeStatutes[0])

print visitedStatutes