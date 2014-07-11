def tokens_sentence(raw_txt):
    tokenize=raw_txt.split(". ")
    tokenize=raw_txt.split("?")
    tokenize=raw_txt.split("!")
    return tokenize
def tokens(sentence):
	tokenize=sentence.split(" ")
        return tokenize
f_in=open('input.txt','r')
f_out=open("output0.txt",'w')
f_out1=open("output1.txt",'w')

context=f_in.read()
sentence=tokens_sentence(context)
print sentence
for item in sentence:
	k = tokens(item)
	for item1 in k:
        	f_out1.write(item1+"\n")
	f_out.write(item+"\n")
f_out.close()
f_out1.close()

