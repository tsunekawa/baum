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
if !mode:
  mode = "flat"

dirpath = options.inputs
output  = options.output
number = int(options.n)
list = os.listdir(dirpath)
result = {}
phrases = []

if(output):
  sys.stdout = open(output, 'w')

# すべてのファイルに対して集計処理を行う
for filename in list:
  # 本文の抽出
  content = extract.extract(os.path.join(dirpath,filename))
  # フレーズの抽出と集計
  for sentence in content['body']:
    phrases += map((lambda x: " ".join(x)),extract.make_phrase(sentence,number))

result = freq.freq_tally(phrases).items()
result = sorted(result, key=lambda x:int(x[1]), reverse=True)

if mode=="flat":
  result = operation.flat(dirpath)
elif mode=="hierachical"
  result = operation.hierachical(dirpath)
else
  raise 'mode should be flat or hierachical'

threshold = int(options.t)

for item in result:
  if item[1]>=threshold:
    print item[0]+" : "+str(item[1]["count"])
