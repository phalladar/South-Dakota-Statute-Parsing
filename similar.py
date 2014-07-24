# coding=utf-8
import difflib, pickle, HTMLParser

web = pickle.load(open("web_complete.p")).decode('ascii', 'ignore')