import nltk
import string
import numpy
from numpy import *
from nltk.corpus import wordnet as wn

def summary():
	# Paragraph splitting
	fil=open('output2.txt','r')
	fil =fil.read().lower()
	# Remove punctuations
	fil = fil.translate(string.maketrans("",""), string.punctuation)
	para=fil.split('\n\n')
	print "\n No of paragraphs : ",len(para)-1
	#print para
	l=len(para)-1
	term=[]
	for item in para:
		item=item.split()
		item = [w for w in item if not w in nltk.corpus.stopwords.words('english')]
		stemmer = nltk.PorterStemmer()
		item = [stemmer.stem(word) for word in item]
		item =list (set(nltk.FreqDist(item)))
		term.append(item)

	##print term


	## Paragraph paragraph corelation matrix
	tlen = len(term)
	dlen = len(term)
	#print tlen
	#print dlen
	A = numpy.zeros((tlen, dlen))
	for i,t in enumerate(term):
		for j,d in enumerate(term):
			A[i,j] = len(set(t)&set(d) )
			if i==j:
				A[i,j]=0

	print "\n##	Paragraph Paragraph Relationship	##\n"
	print A
	colsum= map(sum,zip(*A))
	print "\n Maximum coloumn sum : ",colsum
	m=max(colsum)
	print m

	p=100
	for i,t in enumerate(colsum):
		if (t==m):
			if(p>i):
				p=i
	#print "\n Most important sentence :",p+1,"\n\n",para[p]
	f_out=open("output4.txt",'w+')
	s=[]
	s.append(0)
	out=para[0]
	print out
	f_out.write(out+"\n\n")
	print para[p]
	#array=[]
	out=para[p]
	#array.append(out)
	f_out.write(out+"\n\n")
	s=[]
	s.append(p)
	print  "answer",s.count(p)

	#for printing sentences
	var=0
	i=0
	j=0
	n=l/2
	temp=0
	while(i<n-2):
		j=0	
		while(j<l):
			if(colsum[j]>temp):
				if(s.count(j)==0):
					#print "ans",colsum[j]
					temp=colsum[j]	
					var=j
			j+=1
		#m=temp
		s.append(var)
		temp=0
		i+=1
		out=para[var]
		f_out.write(out+"\n\n")
		#array.append(out)
		print "\n",para[var]
		print  "answer",s.count(var)
	
	f_out.close()

	#print array



