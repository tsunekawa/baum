#!/opt/local/bin/python2.7
#-*- coding:utf-8 -*-
# nlist.py

from ngram import ngram

def nlist(arr,n=2):
	nlist=[]
	for text in arr:
		nlist.extend(ngram(text,n))
	return nlist


if __name__ == "__main__":
  texts =["Several methods have been developed for the transfer of chemicals, proteins, and nucleic acids into live cells"," only describes a Gentoo installation using","for your system after which you install all core system packages. To bootstrap"]
  print nlist(texts,n=3)
