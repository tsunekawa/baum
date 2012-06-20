#-*- coding:utf-8 -*-
# ngram.py
# 文字列をN-gramで分割する
def ngram(text,n=2):
  tokens = []
  for i in range(len(text)):
    if i+n <= len(text):
      tokens.append(text[i:i+n])
    else:
      break
  return tokens

if __name__ == "__main__":
  text = "Several methods have been developed for the transfer of chemicals, proteins, and nucleic acids into live cells"
  print "text:"
  print text
  print "n=1:"
  print ngram(text,n=1)
  print "n=2:"
  print ngram(text,n=2)
  print "n=3:"
  print ngram(text,n=3)
