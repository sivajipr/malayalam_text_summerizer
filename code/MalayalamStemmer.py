

def findstem(mal_word):
    files=open('resources/am_karam_endings.ml','r')
    #files=open('resources/am_karam_endings.ml','r')
    am_karam_endings_array = files.read().split("\n")
    files.close()
    files=open('resources/bare_ml_endings.ml','r')
    #files=open('resources/bare_ml_endings.ml','r')
    bare_ml_endings_array =files.read().split('\n')
    files.close()
    
########## AM KAARAM UNICODE ############################################    
    am_karam_endings_unicode_array =[]
    for item in am_karam_endings_array:
        am_karam_unicode =item.decode('UTF-8')
        am_karam_endings_unicode_array.append(am_karam_unicode)
        #print am_karam_unicode
        
######### BARE WORD UNICODE ############################################## 
    bare_ml_endings_unicode_array = []   
    for item in bare_ml_endings_array:
        bare_ml_unicode =item.decode('UTF-8')
        bare_ml_endings_unicode_array.append(bare_ml_unicode.strip())
        #print bare_ml_unicode," len=",len(bare_ml_unicode.strip())
    #print "---------------------"
    
######### INPUT WORD IN UNICODE ###########################################

    am_karam = u'\u0d02'        
    mal_word_unicode = mal_word.decode('UTF-8')
    start_bound = 1
    end_bound = len(mal_word_unicode)
    stemmed_word =""
    for i in range(start_bound,end_bound):
        #print mal_word_unicode[i:end_bound],"i=",i,":::",bare_ml_endings_unicode_array[5] 
        if mal_word_unicode[i:end_bound] in am_karam_endings_unicode_array:
            stemmed_word = mal_word_unicode[0:i]+am_karam
            break
        # print len(mal_word_unicode[i:end_bound]),":::",len(bare_ml_endings_unicode_array[5].strip())
        if mal_word_unicode[i:end_bound] in bare_ml_endings_unicode_array:
            stemmed_word = mal_word_unicode[0:i]
            break
    #print "stemmed_word=" , stemmed_word
    if stemmed_word=="":
        stemmed_word = mal_word_unicode
        
    #print "stemmed_word=" , stemmed_word
    return stemmed_word.encode('UTF-8')

###### STEMMER FUNCTION ENDS ###########    
    
#input_file =open("input.txt","r")
#input_word = input_file.read().strip()  
#findstem(input_word);
