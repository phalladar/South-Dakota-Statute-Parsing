# coding=utf-8
import re, pprint, pickle

theString = open("C:\\sdcode.txt", "r").read()

ddisk_dict = {}

specialStatutes = re.findall(r'(\n(\d*[A-Z]?-\d*[A-Z]?-\d*[\.\d]*[A-Z]?[-\d*[\.\d]*[A-Z]?]?).*(?:Repealed|Superseded|Obsolete|Transferred|Reserved|Rejected|Omitted|Not|Executed)\.).*\n(.*)', theString, re.DOTALL)
#specialStatutes = filter(None, specialStatutes)

for i in specialStatutes:
	i = filter(None, i) # Account for the regex alternatives yielding empty elements (strip them)
	ddisk_dict[i[1]] = i[0]

regularStatutes = re.findall(r'(\n(\d*[A-Z]?-\d*[A-Z]?-\d*[\.\d]*[A-Z]?[-\d*[\.\d]*[A-Z]?]?)(?! (?:Superseded|Repealed|Transferred|Obsolete|Reserved|Rejected|Omitted|Not|Executed)) [^to].*?)\s\s\s+Source:', theString, re.DOTALL)
for j in regularStatutes:
	ddisk_dict[j[1]] = j[0]

for key in ddisk_dict:
	#print key.decode('utf-8', 'ignore')
 	ddisk_dict[key] = re.sub(r'\n\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*.*\n\t +', "", ddisk_dict[key], 1, re.MULTILINE) 
 	ddisk_dict[key] = re.sub(r'\t', "", ddisk_dict[key], re.MULTILINE) 
 	# this is the only way I could find to remove the first instance of the heading -- limit to one match or both instances
 	# would disappear

# Use the below to test specific statutes
print ddisk_dict['34A-3A-6'].decode('utf-8', 'ignore')

# Use the below to pickle dump the entire database
#pickle.dump( ddisk_dict, open("ddisk.p", "wb"))