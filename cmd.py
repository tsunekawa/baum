#!/usr/env python
#-*- coding:utf-8 -*-

import os
import extract,freq,operation
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input", dest="inputs",
		  help="read xmlfiles in DIRECTORY as journal documents",
		  metavar="DIRECTORY")
parser.add_option("-o", "--output", dest="output",
		  help="write result into OUTPUT file",
		  metavar="OUTPUT")
parser.add_option("-n", "--numterms", dest="n",
		  help="set number of terms",
		  metavar="NUMBER")
parser.add_option("-t", "--threshold", dest="t",
		  help="set threshold of counting",
		  metavar="THRESHOLD")

parser.add_option("-F", "--flat",
                  action="store_const", const="flat", dest="mode",
		  help="switch flat mode",
		  metavar="FLATMODE")
parser.add_option("-H", "--hierarchical",
                  action="store_const", const="hierarchical", dest="mode",
		  help="switch hierarchical mode",
		  metavar="HIERMODE")

(options, args) = parser.parse_args()

# モードの指定
mode = options.mode
dirpath = options.inputs
output  = options.output
number = int(options.n)
threshold = int(options.t)
result = {}

if(output):
  sys.stdout = open(output, 'w')

if mode=="flat":
  result = operation.flat(dirpath, number, threshold)
elif mode=="hierachical":
  # result = operation.hierachical(dirpath, number, threshold)
  pass
else:
  raise 'mode should be flat or hierachical'

# 結果をソートして表示
result = sorted(result.items(), key=lambda x:int(x[1]["count"]), reverse=True)
for item in result:
  print item[0]+" : "+str(item[1]["count"])
