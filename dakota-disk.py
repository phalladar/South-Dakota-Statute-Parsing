# coding=utf-8
import re, pprint, pickle

theString = open("C:\\sdcode.txt", "r").read()


ddisk_dict = {}

# x = re.findall(r'\n(\d+[A-Z]?-\d+[A-Z]?-\d+[A-Z]?) [^to](.*?)Source:', theString, re.DOTALL)

# for i in x:
# 	print i[0]

repealed = re.findall(r'\n(\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*)(?= Repealed\.\s*\n) Repealed.\s*\n([^to].*?)\n\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*', theString, re.DOTALL)
for i in repealed:
	ddisk_dict[i[0]] = i[1]

regularStatutes = re.findall(r'(\n(\d*[A-Z]?-\d*[A-Z]?-\d*[\.\d]*[A-Z]?)(?! Repealed) [^to].*?)\s\s\s+Source:', theString, re.DOTALL)
for j in regularStatutes:
	ddisk_dict[j[1]] = j[0]

for key in ddisk_dict:
 	ddisk_dict[key] = re.sub(r'\n\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*.*\n\t +', "", ddisk_dict[key], 1, re.MULTILINE) 
 	ddisk_dict[key] = re.sub(r'\t', "", ddisk_dict[key], re.MULTILINE) 
 	# this is the only way I could find to remove the first instance of the heading -- limit to one match or both instances
 	# would disappear

#print re.sub(r'\n\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*.*\n', "", ddisk_dict['34A-3A-6'], 1, re.MULTILINE).decode('utf-8', 'ignore')
#print re.sub(r'\\n(\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*).*\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]* +', "", ddisk_dict['34A-3A-6'], re.MULTILINE).decode('utf-8', 'ignore')

# Use the below to test specific statutes
#print ddisk_dict['34A-3A-7'].decode('utf-8', 'ignore')

# Use the below to pickle dump the entire database
pickle.dump( ddisk_dict, open("ddisk.p", "wb"))