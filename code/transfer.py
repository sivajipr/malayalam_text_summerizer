import os
KB=[[]]
tx=[]
tg=[]
def read_in_text(string):
	text=string.split()
	'''	
	for i in range(len(text)):
		print text[i].encode('utf-8')
	'''
	f=open("test","w")
	for i in range(len(text)):	
		f.write(text[i].encode('utf-8')+"\n")
	f.close()
def read_in_file(path):
	f=open(path,"r")
	string=f.read()
	text=string.split()
	'''	
	for i in range(len(text)):
		print text[i].encode('utf-8')
	'''
	f=open("test","w")
	for i in range(len(text)):	
		f.write(text[i]+"\n")
	f.close()
	return string
def read_file(path):
	f=open(path,"r")
	string=f.read()
	
	'''	
	for i in range(len(text)):
		print text[i].encode('utf-8')
	'''
	
	f.close()
	return string

def tnt_tagging():
	os.system("./tnt corpus test>temp")
def in_file_tagging():
	f=open("temp","r")
	text=f.read().split("\n")
	f.close()
	f=open("output","w")
	for i in range(len(text)):		
		if not text[i].startswith("%"):
			f.write(text[i]+"\\")
	f.close()
def create_KB_tag_lst():
	f=open("output","r")
	text=f.read().split("\n")
	f.close()	
	global tg
	global tx
	tx=[]
	tg=[]
	for i in range(len(text)):
		if not text[i]=="":
			tx.append(text[i].decode('utf-8'))
			tx[i].split()

			tg.append(tx[i].split()[1])
	'''
	for i in range(len(tx)):
		print tx[i]	
	'''
	return tx
def create_KB_sub_obj(tx):
	global KB
	global tg
	KB=[]
	
	
	KB_temp=['sub_obj','M_F_N','CAT','SG_PL','F_S_T']
	for i in range(len(tx)):
		KB_temp=['','','','','']
		if tg[i].startswith("N_"):
			KB_temp[2]="Noun"	
			if "_S_" in tg[i]:
				KB_temp[0]="Sub"
			elif "_O_" in tg[i]:
				KB_temp[0]="Obj"
			if tg[i].endswith("_M"):
				KB_temp[1]="M"			
			elif tg[i].endswith("_F"):
				KB_temp[1]="F"
			elif tg[i].endswith("_NU"):
				KB_temp[1]="NU"	
			elif "NNP" in tg[i]:
				KB_temp[2]="NNP"	
		elif tg[i].startswith("V_"):
			KB_temp[2]="Verb"
		elif tg[i].startswith("JJ"):
			KB_temp[2]="Adj"
		else:
			KB_temp[2]="Part"					
		KB.append(KB_temp)	
#	KB.remove(KB[0])
#	s=""
#	for i in range(len(KB)):
#		s=s+ KB[i]+"   "+tx[i]+"\n"		
	return KB
'''
read_in_file()
tnt_tagging()
in_file_tagging()
tx=create_KB_tag_lst()
create_KB_sub_obj(tx)
'''
