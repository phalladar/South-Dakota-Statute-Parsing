# coding=utf-8
import re, urllib, htmlentitydefs, pickle, time

def urlToNumber(theURL):
	# Take the URL as input and return the section from it
	return theURL.split('=')[2] 

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

def startCrawlingInitial(website):
	if website != '/':
		for statuteURL in re.findall('''<A HREF="(\/Statutes\/Codified_Laws.*Statute=.*)">\d+[A-Z]?\<\/A>\..*bsp\;(.*)''', urllib.urlopen(website).read(), re.I):
			theTitle = statuteURL[1]
			tempURL = 'http://legis.sd.gov' + statuteURL[0]
			theSection = urlToNumber(tempURL)
			visitedDict[theSection] = {
					'title': re.sub(r'\r', "", theTitle),
					'url': tempURL
				}
			#print "visitedDict['" + theSection + "'] = " + str(visitedDict[theSection])
			if tempURL not in activeStatutes and tempURL not in visitedStatutes and tempURL != '/':
			 	activeStatutes.append(tempURL)
	if website not in visitedStatutes: visitedStatutes.append(website)
	activeStatutes.remove(website)

def startCrawlingNext(website):
	if website != '/':
		for statuteURL in re.findall(ur'A HREF="(\/Statutes.*=\d+.*)\"', urllib.urlopen(website).read(), re.I):
			tempURL = 'http://legis.sd.gov' + statuteURL
			theSection = urlToNumber(tempURL)
			if theSection.find('target') == -1:
				visitedDict[theSection] = {
						'url': tempURL,
						'title': 'PLACEHOLDER'
					}
				#print "visitedDict['" + theSection + "'] = " + str(visitedDict[theSection])
				if tempURL not in activeStatutes and tempURL not in visitedStatutes and tempURL != '/':
				 	activeStatutes.append(tempURL)
	if website not in visitedStatutes: visitedStatutes.append(website)
	activeStatutes.remove(website)

def read_statute(theURL):
    theStatuteNumber = theURL.split(u'&Statute=')[1]

    #theText = theFakeURL #comment this out and uncomment below line when ready to go live
    theText = urllib.urlopen(theURL).read()
    theBodyText = re.findall(ur'<HEAD>(.*)<\/HEAD>', theText, re.DOTALL)

    theTitle =  re.findall(r'<title>(.*\.)\s*<\/title>', theText)

    theBodyText = re.findall(ur'<BODY>(.*)<\/BODY>', theText, re.DOTALL)
    theText = re.sub("&nbsp;", " ", theBodyText[0])
    theText = re.sub(r'(\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*)', r"\1 ", theText, re.DOTALL)
    theText = re.sub('<!-- WP Style Open: IN -->    <!-- WP Style End: IN -->', " ", theText) # account for indents
    theText = re.sub(r'\<!--.*-->', "", theText)
    theText = re.sub(r'<Div.*\">', "", theText) # clear the div
    theText = re.sub(r'\n|<b>|</b>|\r', " ", theText) # remove the newlines
    theText = re.sub(r'<BR>|<br>', r'\n', theText)
    theText = re.sub("<p>", r'\n', theText)
    theText = re.sub(r" +", " ", theText) # Turn all multiple spaces into a single space
    if len(theTitle) == 0:
        theTitle = 'NO_TITLE'
    elif theText.find("Repealed by") != -1:
        theTitle = "Repealed."
    elif theText.find("Supereseded") != -1:
        theTitle = "Supereseded."
    elif theText.find("Obsolete") != -1:
        theTitle = "Obsolete."
    elif theText.find("Repealed") != -1:
        theTitle = "Repealed."
    elif theText.find("Omitted") != -1:
        theTitle = "Omitted."
    else:
        theTitle = theTitle[0][(len(theStatuteNumber) + 1):] # Get rid of the leading statute number and proceeding space
    
    return theStatuteNumber, theText, theTitle

NEEDTOSCRAPE = 'N'

if NEEDTOSCRAPE == 'Y':
	theOldURL = 'http://legis.sd.gov/Statutes/Codified_Laws/default.aspx'

	theMin = '34A'
	theMax = '43'

	activeStatutes = []
	visitedStatutes = []
	visitedDict = {}

	for theNewURL in re.findall('''td\>\<a\shref=\"\/Statutes(.*[^ ]\=(\d*\w*))''', urllib.urlopen(theOldURL).read(), re.I):
		if isAlphaNumInRange(theNewURL[1], theMin, theMax):
			activeStatutes.append('http://legis.sd.gov/Statutes' + unescape(theNewURL[0]))

	while activeStatutes:
		if len(activeStatutes[0].split(' ')) > 1:  # Was seeing some keys with target tags -- this takes care of that
			activeStatutes.remove(activeStatutes[0])
		elif len(activeStatutes[0].split('-')) == 1:
			startCrawlingInitial(activeStatutes[0])
		elif len(activeStatutes[0].split('-')) == 2:
			startCrawlingNext(activeStatutes[0])
			#print "MADE IT\n\n\n\n\n\n\n\n"
		else:
	 		#getStatuteContent(activeStatutes[0])
			#if activeStatutes[0] not in visitedStatutes: visitedStatutes.append(activeStatutes[0])
			#print "Not webcrawling"
			activeStatutes.remove(activeStatutes[0])

	pickle.dump( visitedDict, open("statute-list.p", "wb"))
	#print visitedDict

if NEEDTOSCRAPE == 'N':
	visitedDict = pickle.load(open("statute-list.p", "rb"))
	#print read_statute(visitedDict['34A-3A-6']['url'])
	#theWebStatuteText = visitedDict


	for key in visitedDict:
		print "Beginning " + key + " . . . ."
		if len(visitedDict[key]['url'].split("-")) > 2:
			# ^-- Only repealed Chapters and Statutes (3+ levels out) have text to capture
			theStatNum, theStatText, theStatTitle = read_statute(visitedDict[key]['url'])
			visitedDict[key]['web_text'] = theStatText
			visitedDict[key]['title'] = theStatTitle
			print "Completed " + key
			#pickle.dump( visitedDict, open("in_progress.p", "wb"))
		else:
			visitedDict[key]['web_text'] = 'NONE'
			print "Skipped " + key
			#pickle.dump( visitedDict, open("in_progress.p", "wb"))
	
	pickle.dump( visitedDict, open("in_progress.p", "wb"))