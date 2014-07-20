import pickle

# visitedDict = pickle.load(open("in_progress.p", "rb")) # webpage load

# for key in visitedDict:
# 	print key + ": " + visitedDict[key]['title']

ddiskDict = pickle.load(open("ddisk.p", "rb"))

for key in ddiskDict:
	print ddiskDict[key].decode('utf-8', 'ignore')