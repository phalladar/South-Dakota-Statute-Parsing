# -- coding: utf-8 --
import re, pprint, pickle, HTMLParser
from pprint import pprint
fun = pickle.load(open("similar_dict.p"))
#text_file = open('Output.txt', 'w')

# for i in fun:
# 	print str(i) + '\t' + str(fun[i]['title_similar']) + '\t' + str(fun[i]['text_similar'])

# for i in fun:
# 	if fun[i]['title_similar'] < 90:
# 		try: #assert isinstance(fun[i]['web_title'], str)
# 			print i, fun[i]['title_similar']
# 			print fun[i]['ddisk_title'].decode('utf-8', 'ignore') + ' -- Disk'
# 			print fun[i]['web_title'].decode('utf-8', 'ignore') + ' -- Website'
# 			print '\n'
# 		except Exception:
# 			print 'Problem with ' + i

statuteNum = '41-6-10'
#print "Inapplicability of \xa7\xa7\xa037-5-16 and 37-5-17 where only method of sales is thr...".encode('string_escape')
#print "Inapplicability of \xa7\xa7\xa037-5-16 and 37-5-17 where only method of sales is thr...".decode('utf-8', 'ignore')

# print fun[statuteNum]

#print fun[statuteNum]['ddisk_title']
#print fun[statuteNum]['web_title']

pprint (fun[statuteNum]['ddisk_text'])
print '\n'
pprint (fun[statuteNum]['web_text'])


#text_file.close