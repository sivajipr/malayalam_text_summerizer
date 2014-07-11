f_in = open('output', 'r')
text = f_in.read()
f_in.close()
word_list={}
word_list=text.split("\\")
#for word in word_list:
	#print word

#no_of_words=len(word_list)
w={}
dict_ana={}
dict ={'N_NN_S_NU':'null'}
print len(word_list)
for word in word_list:
	w=word.split()
	str1=""
	if word is str1:
		w=['null','null']
		
	l=len(w)
	#print w[1]
	str2='null'
	if w[0] is str2:
		break
	str3=w[1]
	if(str3.startswith("N_")):
		if str3 is ("N_NN_S_NU"):
			dict['N_NN_S_NU']=w[0]
			print "result" , dict['N_NN_S_NU']
		
	else:
		continue	



