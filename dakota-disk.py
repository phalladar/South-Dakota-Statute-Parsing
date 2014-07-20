# coding=utf-8
import re, pprint, pickle

theString = open("C:\\sdcode.txt", "r").read()

ddisk_dict = {}

specialStatutes = re.findall(r'\n(\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*)(?= Repealed\.\s*\n) Repealed.\s*\n([^to].*?)\n\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*|\n(\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*)(?= Superseded\.\s*\n) Superseded.\s*\n([^to].*?)\n\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*|\n(\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*)(?= Obsolete\.\s*\n) Obsolete.\s*\n([^to].*?)\n\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*|\n(\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*)(?= Transferred\.\s*\n) Transferred.\s*\n([^to].*?)\n\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*|\n(\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*)(?= Reserved\.\s*\n) Reserved.\s*\n([^to].*?)\n\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*|\n(\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*)(?= Rejected\.\s*\n) Rejected.\s*\n([^to].*?)\n\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*|\n(\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*)(?= Omitted\.\s*\n) Omitted.\s*\n([^to].*?)\n\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*|\n(\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*)(?= Not\.\s*\n) Not.\s*\n([^to].*?)\n\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*|\n(\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*)(?= Executed\.\s*\n) Executed.\s*\n([^to].*?)\n\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*', theString, re.DOTALL)
#specialStatutes = filter(None, specialStatutes)

for i in specialStatutes:
	i = filter(None, i) # Account for the regex alternatives yielding empty elements (strip them)
	ddisk_dict[i[0]] = i[1]

regularStatutes = re.findall(r'(\n(\d*[A-Z]?-\d*[A-Z]?-\d*[\.\d]*[A-Z]?[-\d*[\.\d]*[A-Z]?]?)(?! [Superseded|Repealed|Transferred|Obsolete|Reserved|Rejected|Omitted|implemented]) [^to].*?)\s\s\s+Source:', theString, re.DOTALL)
for j in regularStatutes:
	ddisk_dict[j[1]] = j[0]

for key in ddisk_dict:
 	ddisk_dict[key] = re.sub(r'\n\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*.*\n\t +', "", ddisk_dict[key], 1, re.MULTILINE) 
 	ddisk_dict[key] = re.sub(r'\t', "", ddisk_dict[key], re.MULTILINE) 
 	# this is the only way I could find to remove the first instance of the heading -- limit to one match or both instances
 	# would disappear

# Use the below to test specific statutes
print ddisk_dict['37-6-5.1'].decode('utf-8', 'ignore')

# Use the below to pickle dump the entire database
#pickle.dump( ddisk_dict, open("ddisk.p", "wb"))