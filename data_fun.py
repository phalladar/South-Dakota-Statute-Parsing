# coding=utf-8
import re, pprint, pickle

ddisk = pickle.load(open("ddisk2.p"))
web = pickle.load(open('tagged-statutes-1-34.p'))

theStatute = '9-16-5.7'
print ddisk[theStatute]['ddisk_title']
print web[theStatute]['title']