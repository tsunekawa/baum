#-*- coding:utf-8 -*-
import re
#from xml.etree.ElementTree import ElementTree

def make_phrase(sentence,n):
  p = re.compile(r'\W+')
  pvec = p.split(sentence)
  len_pvec = len(pvec)
  #print len_pvec
  result = []
  for i in range(len_pvec - n + 1):
    result.append(pvec[i:i+n])
  return result

if __name__ == "__main__":
   print make_phrase("t,his is .pmc.sample.xml",8)
