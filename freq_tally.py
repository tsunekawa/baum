#-*-coding:utf-8-*-
#freq_tally.py
#語のリストから頻度の連想配列を返す

def freq_tally(list):
	dic = {}
	for word in list:
		if word in dic:
			dic[word]+=1
		else:
			dic[word]=1
	return dic

if __name__=="__main__":
	lis=["i","am","i","i","a","student"]
	print lis
	d=freq_tally(lis)
	print d


