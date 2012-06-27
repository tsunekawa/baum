#!/usr/env python
#-*- coding:utf-8 -*-
import os
import extract,freq

# コマンド実行時に最初に実行されるメソッド
def cmd(args,options={}):
  dirpath = options.inputs
  list = os.listdir(dirpath)
  file_phrases = []
  result = []

  # すべてのファイルに対して集計処理を行う
  for filename in list:
    print "(((" + filename + ")))"
    print ""
    # 本文の抽出
    content = extract.extract(os.path.join(dirpath,filename))
    phrases = []
    # フレーズの抽出と集計
    for sentence in content['body']:
      phrases += map((lambda x: " ".join(x)),extract.make_phrase(sentence,5))
      tally = freq.freq_tally(phrases).items()
      result = result + tally

  # 集計結果を出力する
  return result

if __name__ == "__main__":
  import sys
  from optparse import OptionParser
  parser = OptionParser()
  parser.add_option("-i", "--input", dest="inputs",
                    help="read xmlfiles in DIRECTORY as journal documents",
                    metavar="DIRECTORY")

  (options, args) = parser.parse_args()
  result = sorted(cmd(args, options=options), key=lambda x:int(x[1]), reverse=True)

  for item in result:
    if item[1]>=3:
      print item[0]+" : "+str(item[1])
