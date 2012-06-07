#-*- coding:utf-8 -*-
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
