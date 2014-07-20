# coding=utf-8
import re, urllib

theURL = 'http://legis.sd.gov/Statutes/Codified_Laws/DisplayStatute.aspx?Type=Statute&Statute=43-21'
test_str = urllib.urlopen(theURL).read()
#test_str = re.sub(r'\r|\n', "", test_str)

print re.findall(ur'A HREF="(\/Statutes.*=\d+.*)\"', test_str)[1]

#print test_str