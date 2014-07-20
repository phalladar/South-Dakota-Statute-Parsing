import re

test = u"http://legis.sd.gov/Statutes/Codified_Laws/DisplayStatute.aspx?Type=Statute&Statute=42.1.352"

def urlToTitle(theURL):
	return theURL.split('=')[2]

print urlToTitle(test)