#-*- coding:utf-8 -*-
import os,sys
sys.path.append(os.pardir)

import extract
import freq

def flat(directryname,n,t):
  result = {}
  dirpath=directryname
  list=os.listdir(dirpath)
  phrases = []

  # すべてのファイルに対して集計処理を行う
  for filename in list:
    # 本文の抽出
    content = extract.extract(os.path.join(dirpath,filename))
    # フレーズの抽出と集計
    for sentence in content['body']:
      phrases += map((lambda x: " ".join(x)),extract.make_phrase(sentence,n))

  result = freq.freq_tally(phrases).items()
  result = sorted(result, key=lambda x:int(x[1]), reverse=True)

  re={}

  for item in result:
    if item[1]>=t:
      re[item[0]]={"count":item[1]}
  return re

if __name__ == "__main__":
  print flat("../test/samples/Asia_Pac_Allergy/",3,5)
