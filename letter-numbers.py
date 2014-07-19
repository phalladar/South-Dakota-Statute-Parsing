import re, pprint
pp = pprint.PrettyPrinter(indent=4)

def isAlphaNumInRange(theSection, theMin, theMax):
	print theMin
	print theMax

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



	print 'theMin = ' + str(theMin)
	print 'theMax = ' + str(theMax)
	print 'theValue = ' + str(theValue)

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

# def convertAlphaNum(alphanum):


# 	solveIt = re.findall(r'(\d+)(\w)?', alphanum)
# 	for i in solveIt:
# 		#print i

# 		# print convertAlpha(i[1]) # the converted num
# 		if i[1]:
# 			return float(i[0]) + convertAlpha(i[1]), alphanum # the new number
# 		else:
# 			return float(i[0]), alphanum


print isAlphaNumInRange('34B', '34A', '42')

# orderMe = []

# orderMe.append(convertAlphaNum('112Z'))
# orderMe.append(convertAlphaNum('1'))
# orderMe.append(convertAlphaNum('2'))
# orderMe.append(convertAlphaNum('3A'))
# orderMe.append(convertAlphaNum('6'))
# orderMe.append(convertAlphaNum('2B'))
# orderMe.append(convertAlphaNum('3F'))
# orderMe.append(convertAlphaNum('22G'))
# orderMe.append(convertAlphaNum('23'))
# orderMe.append(convertAlphaNum('18'))
# orderMe.append(convertAlphaNum('7K'))
# orderMe.append(convertAlphaNum('5'))
# orderMe.append(convertAlphaNum('5A'))
# orderMe.append(convertAlphaNum('5B'))
# orderMe.append(convertAlphaNum('5C'))
# orderMe.append(convertAlphaNum('5D'))
# orderMe.append(convertAlphaNum('5E'))
# orderMe.append(convertAlphaNum('5F'))
# orderMe.append(convertAlphaNum('5G'))
# orderMe.append(convertAlphaNum('5H'))
# orderMe.append(convertAlphaNum('5I'))
# orderMe.append(convertAlphaNum('5J'))
# orderMe.append(convertAlphaNum('5K'))
# orderMe.append(convertAlphaNum('5L'))
# orderMe.append(convertAlphaNum('5M'))
# orderMe.append(convertAlphaNum('5N'))
# orderMe.append(convertAlphaNum('5O'))
# orderMe.append(convertAlphaNum('5P'))
# orderMe.append(convertAlphaNum('5Q'))
# orderMe.append(convertAlphaNum('5R'))
# orderMe.append(convertAlphaNum('5S'))
# orderMe.append(convertAlphaNum('5T'))
# orderMe.append(convertAlphaNum('5U'))
# orderMe.append(convertAlphaNum('5V'))
# orderMe.append(convertAlphaNum('5W'))
# orderMe.append(convertAlphaNum('5X'))
# orderMe.append(convertAlphaNum('5Y'))
# orderMe.append(convertAlphaNum('5Z'))


# orderMe.sort()
# pp.pprint(orderMe)