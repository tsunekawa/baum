#-*- coding:utf-8 -*-
import os

# コマンド実行時に最初に実行されるメソッド
def cmd(args,options={}):
  dirpath = options.directory
  list = os.listdir(dirpath)

  # すべてのファイルに対して集計処理を行う
  for filename in list:
    print "(((" + filename + ")))"
    print ""
    print extract.extract(filename)

  # 集計結果を出力する

if __name__ == "__main__":
  import sys
  from optparse import OptionParser
  parser = OptionParser()
  parser.add_option("-d", "--directory", dest="directory",
                    help="read xmlfiles in DIRECTORY as journal documents",
                    metavar="DIRECTORY")

  (options, args) = parser.parse_args()
  cmd(args, options=options)
