#-*- coding:utf-8 -*-
from extract import extract

def freqs(text):
  freqs   = {}
  for word in text.split():
    if word in freqs:
      freqs[word]+=1
    else:
      freqs[word] =1

  return freqs

if __name__ == "__main__":
  def rec_concat(L):
    if L == [] : return []
    else       : return L[0] + rec_concat(L[1:])

  para   = rec_concat(extract("pmc_sample.xml").values())
  freq_list = freqs("".join(para))
  for word,count in sorted(freq_list.items(),key=lambda x:x[1]):
    print word+" : "+str(count)
