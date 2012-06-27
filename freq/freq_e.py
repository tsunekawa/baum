#!/opt/local/bin/python2.7
#-*- coding:utf-8 -*-
# freq_e.py
import sys,os
sys.path.append(os.pardir)

from ngram import ngram
from ngram import nlist
def freq_e(el,n,strs):
  source = nlist(strs,n)
  i = 0
  for term in source:
    if term == el:
      i = i + 1
  return i

if __name__ == "__main__":
  strs = ['ghram','n-ghramgh','ghram-positive']
  print freq_e('gh',2,strs)
