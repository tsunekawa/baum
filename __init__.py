#-*- coding:utf-8 -*-
from xml.etree.ElementTree import ElementTree

def extract(filename):
  e = ElementTree(file=open(filename))
  xpathes = {'abstract':".//abstract//p",'body':"./body//p"}
  results = {}

  for key in xpathes.keys():
    results[key] = []
    for element in e.getroot().findall(xpathes[key]):
      try:
        results[key].append(element.text.encode('utf_8'))
      except:
        pass

  return results

# ngram.py
# 文字列をN-gramで分割する
def ngram(text,n=2):
  token  = []
  tokens = []
  for (i,w) in enumerate(text):
    token.append(w)
    if len(token) >= n or i==(len(text)-1):
      tokens.append("".join(map(str,token)))
      token = []
  return tokens

def freqs(text):
  freqs   = {}
  for word in text.split():
    if word in freqs:
      freqs[word]+=1
    else:
      freqs[word] =1

  return freqs
