#! C:\python27
import re, urllib, pickle

def read_statute_special(theURL):
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
    if theText.find("Repealed by") != -1:
        theTitle = "Repealed."
    elif theText.find("Supereseded") != -1:
        theTitle = "Supereseded."
    elif theText.find("Obsolete") != -1:
        theTitle = "Obsolete."2147
    elif theText.find("Repealed") != -1:
        theTitle = "Repealed."
    elif theText.find("Omitted") != -1:
        print "YES"
        theTitle = "Omitted."
    else:
        theTitle = theTitle[0][(len(theStatuteNumber) + 1):] # Get rid of the leading statute number and proceeding space
    
    return theStatuteNumber, theText, theTitle

theWebStatute = {}
#theWebStatute['35-4-2.10'] = read_statute_special('http://legis.sd.gov/Statutes/Codified_Laws/DisplayStatute.aspx?Type=Statute&Statute=35-4-2.10', '35-4-2.10')
#theWebStatute['34A-3A-6'] = read_statute_special('http://legis.sd.gov/Statutes/Codified_Laws/DisplayStatute.aspx?Type=Statute&Statute=34A-3A-6')

theStatNum, theStatText, theStatTitle = read_statute_special('http://legis.sd.gov/Statutes/Codified_Laws/DisplayStatute.aspx?Type=Statute&Statute=35-5-3.1')
print theStatNum
print theStatText
print theStatTitle



#pickle.dump( theWebStatute, open("webstatutes.p", "wb"))