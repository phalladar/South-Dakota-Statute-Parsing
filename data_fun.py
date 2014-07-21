# coding=utf-8
import re, pprint, pickle

fun = pickle.load(open("similar_dict.p"))

print sorted(fun.items(), key=lambda x: x[1])