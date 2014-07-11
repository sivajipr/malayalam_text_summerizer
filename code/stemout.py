import MalayalamStemmer as mal
f_in=open('output1.txt','r')
words=f_in.read().split('\n')
f_out=open('output2.txt','w')
for item in words:
	stem=mal.findstem(item)
	f_out.write(stem+"\n")
f_out.close()

	
