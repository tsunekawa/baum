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

if __name__ == "__main__":
   print extract("../test/samples/Asia_Pac_Allergy/Asia_Pac_Allergy_2011_Apr_26_1(1)_2-11.nxml")
